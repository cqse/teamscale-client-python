from __future__ import absolute_import
from __future__ import unicode_literals

import requests
from requests.auth import HTTPBasicAuth
import time

import simplejson as json

from teamscale_client.data import ServiceError, Baseline, ProjectInfo
from teamscale_client.utils import to_json


class TeamscaleClient:
    """Basic Python service client to access Teamscale's REST Api.

    Request handling done with:
    http://docs.python-requests.org/en/latest/

    Args:
        url (str): The url to Teamscale (including the port)
        username (str): The username to use for authentication
        password (str): The password/api key to use for authentication
        project (str): The project on which to work
        sslverify: See requests' verify parameter in http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        timeout (float): TTFB timeout in seconds, see http://docs.python-requests.org/en/master/user/quickstart/#timeouts
        branch: The branch name for which to upload/retrieve data
    """

    def __init__(self, url, username, password, project, sslverify=True, timeout=30.0, branch=None):
        self.url = url
        self.username = username
        self.auth_header = HTTPBasicAuth(username, password)
        self.project = project
        self.sslverify = sslverify
        self.timeout = timeout
        self.branch = branch
        self.check_api_version()

    def check_api_version(self):
        """Verifies the server's api version and connectivity.

        Raises:
            ServiceError: If the version does not match or the server cannot be found.
        """
        url = self.get_global_service_url('service-api-info')
        response = self.get(url)
        apiVersion = response.json()['apiVersion']
        if apiVersion < 2:
            raise ServiceError("Server api version " + str(
                apiVersion) + " too low and not compatible. This client requires Teamscale 3.0 or newer.");

    def get(self, url, parameters=None):
        """Sends a GET request to the given service url.

        Args:
            url (str):  The URL for which to execute a PUT request
            parameters (dict): parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = {'Accept': 'application/json'}
        response = requests.get(url, params=parameters, auth=self.auth_header, verify=self.sslverify, headers=headers,
                                timeout=self.timeout)
        if response.status_code != 200:
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
        headers = {'Accept': 'application/json','Content-Type': 'application/json'}
        response = requests.put(url, params=parameters, json=json, data=data,
                                headers=headers, auth=self.auth_header,
                                verify=self.sslverify, timeout=self.timeout)
        if response.status_code != 200:
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
        if response.status_code != 200:
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
        url = self.get_global_service_url('external-findings-group')
        payload = [{'groupName': name, 'mapping': mapping_pattern}]
        return self.put(url, payload)

    def add_finding_descriptions(self, descriptions):
        """Adds descriptions of findings.

        Args:
            descriptions (list): List of :class:`FindingDescription` to add to Teamscale.
        Returns:
            requests.Response: request's response
        """

        url = self.get_global_service_url('add-external-finding-descriptions')
        payload = [{'typeId': d.typeid, 'description': d.description, 'enablement': d.enablement} for d in descriptions]
        return self.put(url, payload)

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
        service_url = self.get_project_service_url("external-report")
        parameters = {
            "t": self._get_timestamp_parameter(timestamp),
            "message": message,
            "partition": partition,
            "format": coverage_format,
            "adjusttimestamp": "true"
        }
        multiple_files = [('report', open(filename, 'rb')) for filename in coverage_files]
        response = requests.post(service_url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                 files=multiple_files, timeout=self.timeout)
        if response.status_code != 200:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
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
            "message": message
        }
        architecture_files = [(path, open(filename, 'rb')) for path, filename in architectures.items()]
        response = requests.post(service_url, params=parameters, auth=self.auth_header, verify=self.sslverify,
                                 files=architecture_files, timeout=self.timeout)
        if response.status_code != 200:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
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
        if response.status_code != 200:
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
        service_url = self.get_global_service_url("projects")
        parameters = {
            "detail": True
        }
        response = self.get(service_url, parameters)
        return [
            ProjectInfo(project_id=x['id'], name=x['name'], description=x['description'],
                        creation_timestamp=x['creationTimestamp'], alias=x.get('alias'),
                        deleting=x['deleting'], reanalyzing=x['reanalyzing']) for x in response.json()]

    def create_project(self, project_configuration):
        """Creates a project with the specified configuration in Teamscale.

        Args:
            project_configuration (data.ProjectConfiguration): The configuration for the project to be created.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self._add_project(project_configuration, perfrom_update_call=False)

    def update_project(self, project_configuration):
        """Updates an existing project in Teamscale with the given configuration. The id of the existing project is
        taken from the configuration.

        Args:
            project_configuration (data.ProjectConfiguration): The configuration for the project to be updated.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self._add_project(project_configuration, perfrom_update_call=True)

    def _add_project(self, project_configuration, perfrom_update_call):
        """Adds a project to Teamscale. The parameter `perfrom_update_call` specifies, whether an update call should be
        made:
        - If `perfrom_update_call` is set to `True`, re-adding a project with an existing id will update the original
        project.
        - If `perfrom_update_call` is set to `False`, re-adding a project with an existing id will result in an error.
        - Further, if `perfrom_update_call` is set to `True`, but no project with the specified id exists, an error is
        thrown as well.

        Args:
            project_configuration (data.ProjectConfiguration): The project that is to be created (or updated).
            perfrom_update_call (bool): Whether to perform an update call.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        service_url = self.get_global_service_url("create-project")
        parameters = {
            "only-config-update": perfrom_update_call
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

    def _get_timestamp_parameter(self, timestamp):
        """Returns the timestamp parameter. Will use the branch parameter if it is set.

        Args:
            timestamp (datetime.datetime): The timestamp to convert

        Returns:
            str: timestamp in ms
        """
        timestamp_seconds = time.mktime(timestamp.timetuple())
        timestamp_ms = str(int(timestamp_seconds * 1000))
        if self.branch is not None:
            return self.branch + ":" + timestamp_ms
        return timestamp_ms

    def get_global_service_url(self, service_name):
        """Returns the full url pointing to a global service.

        Args:
           service_name(str): the name of the service for which the url should be generated

        Returns:
            str: The full url
        """
        return "%s/%s/" % (self.url, service_name)

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
            The parsed JSON data."""
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data
