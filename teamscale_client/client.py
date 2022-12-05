from __future__ import absolute_import
from __future__ import unicode_literals

import os

import requests
from requests.auth import HTTPBasicAuth
import time
import io

import simplejson as json

from teamscale_client.data import ServiceError, Baseline, ProjectInfo, Finding, Task
from teamscale_client.utils import to_json


class TeamscaleClient:
    """Basic Python service client to access Teamscale's REST Api.

    Request handling done with:
    http://docs.python-requests.org/en/latest/

    Args:
        url (str): The url to Teamscale (including the port)
        username (str): The username to use for authentication
        access_token (str): The IDE access token to use for authentication
        project (str): The id of the project on which to work
        sslverify: See requests' verify parameter in http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        timeout (float): TTFB timeout in seconds, see http://docs.python-requests.org/en/master/user/quickstart/#timeouts
        branch (str): The branch name for which to upload/retrieve data
    """

    def __init__(self, url, username, access_token, project, sslverify=True, timeout=30.0, branch=None):
        """Constructor
        """
        self.url = url
        self.username = username
        self.auth_header = HTTPBasicAuth(username, access_token)
        self.project = project
        self.sslverify = sslverify
        self.timeout = timeout
        self.branch = branch
        self.check_api_version()

    @staticmethod
    def from_client_config(config, sslverify=True, timeout=30.0, branch=None):
        """Creates a new Teamscale client from a `TeamscaleClientConfig` object.

        Args:
            config (teamscale_client_config.TeamscaleClientConfig): The client configuration to use.
            sslverify: See requests' verify parameter in http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
            timeout (float): TTFB timeout in seconds, see http://docs.python-requests.org/en/master/user/quickstart/#timeouts
            branch (str): The branch name for which to upload/retrieve data
        """
        return TeamscaleClient(config.url, config.username, config.access_token, config.project_id,
                               sslverify, timeout, branch)

    def set_project(self, project):
        """Sets the project id for subsequent calls made using the client."""
        self.project = project

    def check_api_version(self):
        """Verifies the server's api version and connectivity.

        Raises:
            ServiceError: If the version does not match or the server cannot be found.
        """
        url = self.get_global_service_url('service-api-info')
        response = self.get(url)
        json_response = response.json()
        api_version = json_response['apiVersion']
        if api_version < 6:
            raise ServiceError("Server api version " + str(
                api_version) + " too low and not compatible. This client requires Teamscale 4.1 or newer.")

    def get(self, url, parameters=None):
        """Sends a GET request to the given service url.

        Args:
            url (str):  The URL for which to execute a GET request
            parameters (dict): parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = {'Accept': 'application/json'}
        response = requests.get(url, params=parameters, auth=self.auth_header, verify=self.sslverify, headers=headers,
                                timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=url, r=response))
        return response

    def put(self, url, json=None, parameters=None, data=None):
        """Sends a PUT request to the given service url with the json payload as content.

        Args:
            url (str):  The URL for which to execute a PUT request
            json: The Object to attach as content, will be serialized to json (only for object that can be serialized by default)
            parameters (dict): parameters to attach to the url
            data: The data object to be attached to the request

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.put(url, params=parameters, json=json, data=data,
                                headers=headers, auth=self.auth_header,
                                verify=self.sslverify, timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: PUT {url}: {r.status_code}:{r.text}".format(url=url, r=response))
        return response

    def delete(self, url, parameters=None):
        """Sends a DELETE request to the given service url.

        Args:
            url (str):  The URL for which to execute a DELETE request
            parameters (dict): parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        response = requests.delete(url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                   timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: PUT {url}: {r.status_code}:{r.text}".format(url=url, r=response))
        return response

    def add_findings_group(self, name, mapping_pattern):
        """Adds group of findings.

        Args:
            name (str): Name of group.
            mapping_pattern (str): Regular expression to match a finding's ``typeid`` in order to belong to this group.
        Returns:
            requests.Response: request's response
        """
        url = "%s/%s" % (self.get_global_service_url('external-findings-group'), name)
        return self.put(url, {'groupName': name, 'mapping': mapping_pattern})

    def add_finding_descriptions(self, descriptions):
        """Adds descriptions of findings.

        Args:
            descriptions (list): List of :class:`FindingDescription` to add to Teamscale.
        Returns:
            requests.Response: request's response
        """
        base_url = self.get_global_service_url('external-findings-description')
        response = None
        for finding_description in descriptions:
            some_description = dict()
            some_description['typeId'] = finding_description.typeid
            some_description['description'] = finding_description.description
            some_description['enablement'] = finding_description.enablement
            some_description['name'] = finding_description.name
            url = "%s/%s" % (base_url, finding_description.typeid)
            response = self.put(url, some_description)
            if response.text != 'success':
                return response

        return response

    def update_findings_schema(self):
        """Triggers refresh of finding groups in analysis profiles."""
        url = self.get_global_service_url('update-findings-schema')
        return self.get(url, {'projects': self.project})

    def upload_findings(self, findings, timestamp, message, partition):
        """Uploads a list of findings

        Args:
            findings (List[:class:`data.FileFindings`]): the findings data 
            timestamp (datetime.datetime): timestamp for which to upload the findings
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the findings should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("add-external-findings", findings, timestamp, message, partition)

    def upload_metrics(self, metrics, timestamp, message, partition):
        """Uploads a list of metrics

        Args:
            metrics (List[:class:`data.MetricEntry`]): metrics data
            timestamp (datetime.datetime): timestamp for which to upload the metrics
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the metrics should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("add-external-metrics", metrics, timestamp, message, partition)

    def _upload_external_data(self, service_name, json_data, timestamp, message, partition):
        """Uploads externals data in json format

        Args:
            service_name (str): The service name to which to upload the data
            json_data: data in json format
            timestamp (datetime.datetime): timestamp (unix format) for which to upload the data
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the data should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url(service_name)
        parameters = {
            "t": self._get_timestamp_parameter(timestamp),
            "message": message,
            "partition": partition,
            "skip-session": "true",
            "adjusttimestamp": "true"
        }
        return self.put(service_url, parameters=parameters, data=to_json(json_data))

    def add_metric_descriptions(self, metric_descriptions):
        """Uploads metric definitions to Teamscale.

        Args:
            metric_descriptions (list[:class:`MetricDescription`]): List of metric descriptions to add to Teamscale.

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_global_service_url("external-metric")
        return self.put(service_url, data=to_json(metric_descriptions))

    def upload_coverage_data(self, coverage_files, coverage_format, timestamp, message, partition):
        """Upload coverage reports to Teamscale. It is expected that the given coverage report files can be read from the filesystem.

        Args:
            coverage_files (list): list of coverage filenames (strings!) that should be uploaded. Files must be readable.
            coverage_format  (constants.CoverageFormats): the format to use
            timestamp (datetime.datetime): timestamp (unix format) for which to upload the data
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the data should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.upload_report(coverage_files, coverage_format, timestamp, message, partition)

    def upload_report(self, report_files, report_format, timestamp, message, partition, move_to_last_commit=True):
        """Upload reports from external tools to Teamscale. It is expected that the given report files can be read from
           the filesystem.

        Args:
            report_files (list): list of filenames (strings!) that should be uploaded. Files must be readable.
            report_format  (constants.ReportFormats): the format to use
            timestamp (datetime.datetime): timestamp (unix format) for which to upload the data
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the data should be added
                            (See also: :ref:`FAQ - Partitions<faq-partition>`).
            move_to_last_commit (bool): True to automatically adjust this commit to be the latest otherwise False.
                                        Default is True
        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("external-report")
        parameters = {
            "t": self._get_timestamp_parameter(timestamp),
            "message": message,
            "partition": partition,
            "format": report_format,
            "adjusttimestamp": "true",
            "movetolastcommit": str(move_to_last_commit).lower()
        }
        multiple_files = []
        for filename in report_files:
            with open(filename, 'rb') as inputfile:
                dataobj = io.BytesIO(inputfile.read())
                multiple_files.append(('report', (os.path.basename(filename), dataobj)))
        response = requests.post(service_url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                 files=multiple_files, timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: POST {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return response

    def upload_architectures(self, architectures, timestamp, message):
        """Upload architectures to Teamscale. It is expected that the given architectures can be be read from the filesystem.

        Args:
            architectures (dict): mappping of teamscale paths to architecture files that should be uploaded. Files must be readable.
            timestamp (datetime.datetime): timestamp for which to upload the data
            message (str): The message to use for the generated upload commit

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("architecture-upload")
        parameters = {
            "t": self._get_timestamp_parameter(timestamp),
            "adjusttimestamp": "true",
            "message": message
        }
        architecture_files = [(path, open(filename, 'rb')) for path, filename in architectures.items()]
        response = requests.post(service_url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                 files=architecture_files, timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: POST {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return response

    def upload_non_code_metrics(self, metrics, timestamp, message, partition):
        """Uploads a list of non-code metrics

        Args:
            metrics (List[:class:`data.NonCodeMetricEntry`]): metrics data
            timestamp (datetime.datetime): timestamp for which to upload the metrics
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the metrics should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("add-non-code-metrics", metrics, timestamp, message, partition)

    def get_baselines(self):
        """Retrieves a list of baselines from the server for the currently active project.

        Returns:
            List[:class:`data.Baseline`]): The list of baselines.

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("baselines")
        parameters = {
            "detail": True
        }
        headers = {'Accept': 'application/json'}
        response = requests.get(service_url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                headers=headers, timeout=self.timeout)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return [Baseline(x['name'], x['description'], timestamp=x['timestamp']) for x in response.json()]

    def delete_baseline(self, baseline_name):
        """Deletes a baseline from the currently active project.

        Args:
            baseline_name (string): The baseline that is to be removed.

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("baselines")
        service_url += baseline_name
        return self.delete(service_url, parameters={})

    def add_baseline(self, baseline):
        """Adds a baseline to the currently active project. Re-adding an existing baseline will update the original baseline.

        Args:
            baseline (data.Baseline): The baseline that is to be added (or updated)

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("baselines")
        service_url += baseline.name
        return self.put(service_url, parameters={}, data=to_json(baseline))

    def get_projects(self):
        """Retrieves a list of projects from the server.

        Returns:
            List[:class:`data.ProjectInfo`]): The list of projects.

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_global_service_url_versioned("projects", "v5.6.0")

        parameters = {
            "detail": True
        }
        response = self.get(service_url, parameters)
        return [
            ProjectInfo(project_id=x['id'], name=x['name'], description=x.get('description'),
                        creation_timestamp=x['creationTimestamp'], alias=x.get('alias'),
                        deleting=x['deleting'], reanalyzing=x['reanalyzing']) for x in response.json()]

    def create_project(self, project_configuration, skip_project_validation=False):
        """Creates a project with the specified configuration in Teamscale. The parameter `skip_project_validation`
        specifies, whether to skip the validation of the project.

        Args:
            project_configuration (data.ProjectConfiguration): The configuration for the project to be created.
            skip_project_validation (bool): Whether to skip validation of the project.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self._add_project(project_configuration, skip_project_validation, perform_update_call=False)

    def update_project(self, project_configuration, skip_project_validation=False):
        """Updates an existing project in Teamscale with the given configuration. This may trigger a reanalysis of the
         project if the changes require it. The id of the existing project is taken from the configuration.
         The parameter `skip_project_validation` specifies, whether to skip the validation of the project.

        Args:
            project_configuration (data.ProjectConfiguration): The configuration for the project to be updated.
            skip_project_validation (bool): Whether to skip validation of the project.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self._add_project(project_configuration, skip_project_validation, perform_update_call=True)

    def _add_project(self, project_configuration, skip_project_validation, perform_update_call):
        """Adds a project to Teamscale. The parameter `skip_project_validation` specifies, whether to skip the validation of the project.
        The parameter `perform_update_call` specifies, whether an update call should be made:
        - If `perform_update_call` is set to `True`, re-adding a project with an existing id will update the original
        project.
        - If `perform_update_call` is set to `False`, re-adding a project with an existing id will result in an error.
        - Further, if `perform_update_call` is set to `True`, but no project with the specified id exists, an error is
        thrown as well.

        Args:
            project_configuration (data.ProjectConfiguration): The project that is to be created (or updated).
            skip_project_validation (bool): Whether to skip validation of the project.
            perform_update_call (bool): Whether to perform an update call.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        service_url = self.get_global_service_url("create-project")
        parameters = {
            "skip-project-validation": skip_project_validation,
            "only-config-update": perform_update_call,
            "reanalyze-if-required": True # Otherwise, changes which require a reanalysis would silently be ignored
        }
        response = self.put(service_url, parameters=parameters, data=to_json(project_configuration))

        response_message = TeamscaleClient._get_response_message(response)
        if response_message != 'success':
            raise ServiceError(
                "ERROR: GET {url}: {status_code}:{message}".format(url=service_url, status_code=response.status_code,
                                                                   message=response_message))
        return response

    @staticmethod
    def _get_response_message(response):
        """Returns the message enclosed in the provided server response.

        Args:
            response (requests.Response): The server response.

        Returns:
            A string containing the server response message.
        """
        return response.json().get('message')

    def _get_timestamp_parameter(self, timestamp, branch=None):
        """Returns the timestamp parameter. Will use the branch parameter if it is set.
        Returned timestamp is 'HEAD' if given timestamp is `None`.

        Args:
            timestamp (datetime.datetime): The timestamp to convert
            branch (str): The branch to use. If this parameter is not set, the branch that was used to initialize the
                          client is used, if any.

        Returns:
            str: timestamp in ms, optionally prepended by the branch name.
            Returned timestamp is 'HEAD' if given timestamp is `None`.
        """
        timestamp_or_head = 'HEAD'
        if timestamp:
            timestamp_seconds = time.mktime(timestamp.timetuple())
            timestamp_or_head = str(int(timestamp_seconds * 1000))
        default_branch_name = branch if branch else self.branch
        if default_branch_name:
            return default_branch_name + ":" + timestamp_or_head
        return timestamp_or_head

    def get_global_service_url(self, service_name):
        """Returns the full url pointing to a global service.

        Args:
           service_name(str): the name of the service for which the url should be generated

        Returns:
            str: The full url
        """
        return "%s/%s/" % (self.url, service_name)

    def get_global_service_url_versioned(self, service_name, api_version):
        """Returns the full url pointing to a specific version of a global service.

        Args:
           service_name(str): the name of the service for which the url should be generated
           api_version(str): the teamscale api version (e.g. "v5.6.0")

        Returns:
            str: The full url
        """
        return "%s/api/%s/%s/" % (self.url, api_version, service_name)

    def get_project_service_url(self, service_name):
        """Returns the full url pointing to a project service.

        Args:
           service_name(str): the name of the service for which the url should be generated

        Returns:
            str: The full url
        """
        return "{client.url}/p/{client.project}/{service}/".format(client=self, service=service_name)

    @classmethod
    def read_json_from_file(cls, file_path):
        """Reads JSON content from a file and parses it to ensure basic integrity.

        Args:
            file_path (str): File from which to read the JSON content.

        Returns:
            The parsed JSON data.
        """
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data

    def upload_files_for_precommit_analysis(self, timestamp, precommit_data):
        """Uploads the provided files for precommit analysis.

        Args:
            timestamp (datetime.datetime): The timestamp of the parent commit.
            precommit_data (data.PreCommitUploadData): The precommit data to upload.
        """
        service_url = self.get_project_service_url("pre-commit") + self._get_timestamp_parameter(timestamp)

        response = self.put(service_url, data=to_json(precommit_data))
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))

    def get_precommit_analysis_results(self):
        """Gets precommit analysis results.

        Returns:
            A tuple consisting of three lists: added findings, findings in changed code, and removed findings.
        """
        service_url = self.get_project_service_url("pre-commit")

        while True:
            response = self.get(service_url)
            # We need to wait for 200 here to get the findings.
            # The service returns 204 while the pre-commit analysis is still in progress.
            if response.status_code != 200:
                time.sleep(2)
            else:
                return self._parse_findings_response(service_url, response)

    def _parse_findings_response(self, service_url, response):
        """Parses findings retrieved from Teamscale.

        Args:
            service_url (str): The service url. Used for logging.
            response (requests.Response): The response to parse for findings.

        Returns:
            A tuple consisting of three lists: added findings, findings in changed code, and removed findings.

        Raises:
            ServiceError: If anything goes wrong.
        """
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))

        added_findings = self._findings_from_json(response.json()['addedFindings'])
        findings_in_changed_code = self._findings_from_json(response.json()['findingsInChangedCode'])
        removed_findings = self._findings_from_json(response.json()['removedFindings'])

        return added_findings, removed_findings, findings_in_changed_code

    def _findings_from_json(self, findings_json):
        """Parses JSON encoded findings.

        Args:
            findings_json (List[object]): The json object encoding the list of findings.

        Returns:
            List[data.Finding]: The findings that were parsed from the JSON object
        """
        return [self._finding_from_json(finding)
                for finding in findings_json]

    def _finding_from_json(self, finding_json):
        """Parses Ja single SON encoded finding.

        Args:
            finding_json (object): The json object encoding the finding.

        Returns:
            data.Finding: The finding that was parsed from the JSON object
        """
        return Finding(finding_type_id=finding_json['typeId'],
                       message=finding_json['message'],
                       assessment=finding_json['assessment'],
                       start_offset=self._get_finding_location_entry(finding_json, 'rawStartOffset', 0),
                       end_offset=self._get_finding_location_entry(finding_json, 'rawEndOffset', 0),
                       start_line=self._get_finding_location_entry(finding_json, 'rawStartLine', 1),
                       end_line=self._get_finding_location_entry(finding_json, 'rawEndLine', 1),
                       uniform_path=finding_json['location']['uniformPath'],
                       finding_id=finding_json['id'])

    def _get_finding_location_entry(self, finding_json, key, defaultValue):
        """Safely extracts a value from the location data of a JSON encoded finding.
        Some findings don't have all the location data, in which case the given default value
	is returned.

        Args:
            finding_json (object): The json object encoding the finding.
            key (string): The key in the location data to look up.
            defaultValue (object): The default value to return in case the key cannot be found.

        Returns:
            object: The value or the default value.
        """
        value = finding_json['location'].get(key)
        if value is None:
            return defaultValue

        return value

    def get_findings(self, uniform_path, timestamp, recursive=True, revision_id=None, filter=None, invert=False, assessmentFilters=None):
        """Retrieves the list of findings in the currently active project for the given uniform path
        at the provided timestamp on the given branch.

        Args:
            uniform_path (str): The uniform path to get findings for.
            timestamp (datetime.datetime): timestamp (unix format) for which to upload the data
            recursive (bool): Whether to query findings recursively, i.e. also get findings for files under the given
                path.
            revision_id (str): If provided, the client will first resolve the ID (e.g., commit hash) to a Teamscale
               commit and retrieve the findings for the corresponding branch.
            filter: The finding category, group, and type filters. 
                Every string must be either a single category, a combination category/group, or a type ID. 
                If a category or group is given, all matching findings will be filtered out and not included in the result.
            invert: Whether to invert the category, group, type filters, 
                i.e. including the elements given in the filters instead of excluding them.
            assessmentFilters: The assessment filter. All mentioned assessment colors will be filtered out and not included in the result.

        Returns:
            List[:class:`data.Finding`]): The list of findings.

        Raises:
            ServiceError: If anything goes wrong
        """
        if revision_id:
            timestamp = self.get_commit_for_revision(revision_id)
        else:
            timestamp = self._get_timestamp_parameter(timestamp=timestamp)

        service_url = self.get_project_service_url("findings") + uniform_path
        parameters = {
            "t": timestamp,
            "recursive": recursive,
            "all": True
        }

        if filter:
            parameters["filter"] = filter
        if invert:
            parameters["invert"] = True
        if assessmentFilters:
            parameters["assessment-filters"] = assessmentFilters
        response = self.get(service_url, parameters=parameters)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return self._findings_from_json(response.json())

    def get_commit_for_revision(self, revision_id):
        """Retrieves the Teamscale commit corresponding to a revision, raising an error if the commit is not known
        to Teamscale.

        Args:
            revision_id (str) The revision ID (e.g., commit SHA)

        Returns:
            str: The teamscale commit
        """
        service_url = self.get_project_service_url("repository-timestamp-by-revision") + revision_id
        response = self.get(service_url)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))

        response_json = response.json()

        if not response_json:
            raise ServiceError("Could not find commit in Teamscale for given revision: {rev}".format(rev=revision_id))

        return response_json[0]["branchName"] + ":" + str(response_json[0]["timestamp"])

    def get_finding_by_id(self, finding_id, branch=None, timestamp=None):
        """Retrieves the finding with the given id.

        Args:
            finding_id (str): The id of the finding to retrieve.
            branch (str): The branch from which the finding should be retrieved.
            timestamp (datetime.datetime): The timestamp (unix format) for which to receive the finding.

        Returns:
             data.Finding: The retrieved finding.

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("findings-by-id") + finding_id

        parameters = {
            "t": self._get_timestamp_parameter(timestamp=timestamp, branch=branch),
        }
        response = self.get(service_url, parameters=parameters)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return self._finding_from_json(response.json())

    def get_finding_url(self, finding):
        """Returns the full url pointing to the specified finding in Teamscale,
        or `None` if the finding does not have an id.

        Args:
           finding(data.Finding): the finding for which the url should be generated

        Returns:
            str: The full url
        """
        if not finding.finding_id:
            return None
        return "{client.url}/findings.html#details/{client.project}/?id={finding_id}" \
            .format(client=self, finding_id=finding.finding_id)

    def get_tasks(self, status="OPEN", details=True, start=0, max=300):
        """Retrieves the tasks for the client's project from the server.

        Args:
            status (constants.TaskStatus): The status to retrieve tickets for
            details (bool): Whether to retrieve details together with the tasks
            start (number): From which task number to start listing tasks
            max (number): Maximum number of tasks to return

        Returns:
            List[:class:`data.Task`]): The list of tasks.

        Raises:
            ServiceError: If anything goes wrong
            """
        service_url = self.get_project_service_url("tasks")
        parameters = {
            "status": status,
            "details": details,
            "start": start,
            "max": max,
            "with-count": False
        }
        response = self.get(service_url, parameters=parameters)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return TeamscaleClient._tasks_from_json(response.json())

    def add_task_comment(self, task_id, comment):
        """Adds a comment to a task.

        Args:
            task_id (number): the task id to which to add the comment
            comment (str): the comment to add

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        service_url = self.get_project_service_url("comment-task") + str(task_id)
        response = self.put(service_url, data=to_json(comment))
        if not response.ok:
            raise ServiceError("ERROR: PUT {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return response

    @staticmethod
    def _tasks_from_json(task_json):
        """Parses JSON encoded findings.

        Args:
            task_json (List[object]): The json object encoding the list of findings.

        Returns:
            list[data.Task]: The tasks that was parsed from the JSON object
        """
        return [Task.from_json(x) for x in task_json]

    def add_issue_metric(self, name, issue_query):
        """Adds group of findings.

        Args:
            name (str): Name of issue metric
            issue_query (str): The issue query to add
        Returns:
            requests.Response: request's response
        """
        url = "%s/%s" % (self.get_project_service_url('issue-metrics'), name)
        return self.put(url, {'name': name, 'query': issue_query})

    def create_dashboard(self, dashboard_descriptor):
        """Adds a new dashboard from the given template.

        Args:
            dashboard_descriptor (str): The dashboard descriptor that should be uploaded
        Returns:
            requests.Response: request's response
        """
        service_url = self.get_global_service_url("dashboard-export")
        multiple_files = [('dashboardDescriptor', dashboard_descriptor)]
        return requests.post(service_url, auth=self.auth_header, verify=self.sslverify,
                             files=multiple_files, timeout=self.timeout)

    def get_project_configuration(self, project_id):
        """Adds a new dashboard from the given template.

                Args:
                    project_id (str): The id for which the project configuration should be retrieved
                Returns:
                    str: The project configuration as json
                """
        url = "%s%s" % (self.get_global_service_url("create-project"), project_id)
        return self.get(url).json()

    def get_architectures(self):
        """Returns the paths of all architecture in the project.

            Returns:
                List[str] The architecture names.
        """
        service_url = self.get_project_service_url("arch-assessment")
        parameters = {
            "list": True,

        }
        response = self.get(service_url, parameters=parameters)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return [architecture_overview['uniformPath'] for architecture_overview in response.json()]
