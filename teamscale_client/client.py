import datetime
import io
import json
import os
import time
from typing import Dict, Union, List, Optional, Any, Tuple

import requests
from requests.auth import HTTPBasicAuth

from teamscale_client.client_utils import parse_version
from teamscale_client.constants import ReportFormats, CoverageFormats, ArchitectureFormats, Assessment
from teamscale_client.data import ServiceError, Baseline, ProjectInfo, Finding, Task, MetricEntry, FileFindings, \
    FindingDescription, MetricDescription, NonCodeMetricEntry, ProjectConfiguration
from teamscale_client.utils import to_json, to_json_dict


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

    TEAMSCALE_API_VERSION = "v8.0.0"

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

        self._api_url = f"{self.url}/api"
        self._api_url_version = f"{self._api_url}/{TeamscaleClient.TEAMSCALE_API_VERSION}"

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
        return TeamscaleClient(config.url, config.username, config.access_token, config.project_id, sslverify, timeout,
                               branch)

    def set_project(self, project):
        """Sets the project id for subsequent calls made using the client."""
        self.project = project

    def check_api_version(self) -> None:
        """Verifies the server's api version and connectivity.

        Raises:
            ServiceError: If the version does not match or the server cannot be found.
        """
        response = self.get(f"{self._api_url}/version")
        json_response = response.json()
        python_client_api = parse_version(TeamscaleClient.TEAMSCALE_API_VERSION)

        min_supported_api = parse_version(json_response["minApiVersion"])
        if min_supported_api > python_client_api:
            raise ServiceError(
                "The Server API minimally supports {min}, which is too high for this client running {current}".format(
                    min=min_supported_api, current=python_client_api))

        max_supported_api = parse_version(json_response["maxApiVersion"])
        if max_supported_api < python_client_api:
            raise ServiceError(
                "The Server API maximally supports {max}, which is too low for this client running {current}".format(
                    max=max_supported_api, current=python_client_api))

    def get(self, url: str, parameters: Optional[Dict] = None) -> requests.Response:
        """Sends a GET request to the given service url.

        Args:
            url:  The URL for which to execute a GET request
            parameters: parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = {'Accept': 'application/json'}
        response = requests.get(url, params=parameters, auth=self.auth_header, verify=self.sslverify, headers=headers,
                                timeout=self.timeout)
        if not response.ok:
            raise ServiceError(f"ERROR: GET {url}: {response.status_code}:{response.text}")
        return response

    def put(self, url: str, **kwargs) -> requests.Response:
        """Sends a PUT request to the given service url with the json payload as content.

        Args:
            url:  The URL for which to execute a PUT request
            **kwargs: passed to requests library (examples see below)

        Keyword Args:
            json: The Object to attach as content, will be serialized to json
                (only for object that can be serialized by default)
            params: parameters to attach to the url
            data: The data object to be attached to the request


        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = kwargs.get("headers", {'Accept': 'application/json', 'Content-Type': 'application/json'})
        response = requests.put(
            url, headers=headers, auth=self.auth_header, verify=self.sslverify, timeout=self.timeout, **kwargs
        )
        if not response.ok:
            raise ServiceError(f"ERROR: PUT {url}: {response.status_code}:{response.text}")
        return response

    def post(self, url: str, **kwargs) -> requests.Response:
        """Sends a POST request to the given service url with the json payload as content.

        Args:
            url:  The URL for which to execute a POST request
            **kwargs: passed to requests library (examples see below)

        Keyword Args:
            json: The Object to attach as content, will be serialized to json
                (only for object that can be serialized by default)
            params: parameters to attach to the url
            data: The data object to be attached to the request

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        headers = kwargs.pop("headers", {'Accept': 'application/json', 'Content-Type': 'application/json'})
        response = requests.post(
            url, headers=headers, auth=self.auth_header, verify=self.sslverify, timeout=self.timeout, **kwargs
        )
        if not response.ok:
            raise ServiceError(f"ERROR: POST {url}: {response.status_code}:{response.text}")
        return response

    def delete(self, url: str, parameters: Optional[Dict] = None) -> requests.Response:
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
            raise ServiceError(f"ERROR: DELETE {url}: {response.status_code}:{response.text}")
        return response

    def add_findings_group(self, name: str, mapping_pattern: str) -> requests.Response:
        """Adds group of findings.

        Args:
            name: Name of group.
            mapping_pattern: Regular expression to match a finding's ``typeid`` in order to belong to this group.
        Returns:
            requests.Response: request's response
        """
        return self.post(
            f"{self._api_url_version}/external-findings/groups",
            json={'groupName': name, 'mapping': mapping_pattern}
        )

    def add_finding_descriptions(self, descriptions: List[FindingDescription]) -> requests.Response:
        """Adds descriptions of findings.

        Args:
            descriptions: List of :class:`FindingDescription` to add to Teamscale.
        Returns:
            requests.Response: request's response
        """
        response = None
        for finding_description in descriptions:
            response = self.post(
                f"{self._api_url_version}/external-findings/description",
                json=vars(finding_description)
            )
        return response

    def update_findings_schema(self):
        """Triggers refresh of finding groups in analysis profiles."""
        # TODO Ensure that this is the correct replacement for 'update-findings-schema'
        return self.post(f"{self._api_url}/projects/{self.project}/metric-update", {"projects": self.project})

    def upload_findings(
            self, findings: List[FileFindings], timestamp: datetime.datetime, message: str, partition: str
    ) -> requests.Response:
        """Uploads a list of findings

        Args:
            findings: the findings data
            timestamp: timestamp for which to upload the findings
            message: The message to use for the generated upload commit
            partition: The partition's id into which the findings should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("external-findings", to_json(findings), timestamp, message, partition)

    def upload_metrics(
            self, metrics: List[MetricEntry], timestamp: datetime.datetime, message: str, partition: str
    ) -> requests.Response:
        """Uploads a list of metrics

        Args:
            metrics: metrics data
            timestamp: timestamp for which to upload the metrics
            message: The message to use for the generated upload commit
            partition: The partition's id into which the metrics should be added (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("external-metrics", to_json(metrics), timestamp, message, partition)

    def _upload_external_data(
            self, service_name: str, json_data: str, timestamp: datetime.datetime, message: str, partition: str
    ) -> requests.Response:
        """Uploads externals data in json format

        Args:
            service_name: The service name to which to upload the data
            json_data: data in json format
            timestamp: timestamp (unix format) for which to upload the data
            message: The message to use for the generated upload commit
            partition: The partition's id into which the data should be added
                (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.post(
            f"{self._api_url_version}/projects/{self.project}/external-analysis/session/auto-create/{service_name}",
            params={
                "t": self._get_timestamp_parameter(timestamp),
                "message": message,
                "partition": partition
            },
            data=json_data
        )

    def add_metric_descriptions(self, metric_descriptions: List[MetricDescription]) -> requests.Response:
        """Uploads metric definitions to Teamscale.

        Args:
            metric_descriptions: List of metric descriptions to add to Teamscale.

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.post(
            f"{self._api_url_version}/external-metrics",
            json=to_json_dict(metric_descriptions)
        )

    def upload_coverage_data(
            self, coverage_files: List[str], coverage_format: CoverageFormats, timestamp: datetime.datetime,
            message: str, partition: str
    ) -> requests.Response:
        """Upload coverage reports to Teamscale. It is expected that the given coverage report
        files can be read from the filesystem.

        Args:
            coverage_files: list of coverage filenames (strings!) that should be uploaded. Files must be readable.
            coverage_format: the format to use
            timestamp: timestamp (unix format) for which to upload the data
            message: The message to use for the generated upload commit
            partition: The partition's id into which the data should be added
                (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.upload_report(coverage_files, coverage_format, timestamp, message, partition)

    def upload_report(
            self, report_files: List[str], report_format: Union[ReportFormats, CoverageFormats],
            timestamp: datetime.datetime, message: str, partition: str, move_to_last_commit: bool = True
    ) -> requests.Response:
        """Upload reports from external tools to Teamscale. It is expected that the given report files can be read from
           the filesystem.

        Args:
            report_files: list of filenames (strings!) that should be uploaded. Files must be readable.
            report_format: the format to use
            timestamp: timestamp (unix format) for which to upload the data
            message: The message to use for the generated upload commit
            partition: The partition's id into which the data should be added
                            (See also: :ref:`FAQ - Partitions<faq-partition>`).
            move_to_last_commit: True to automatically adjust this commit to be the latest otherwise False.
                                        Default is True
        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        multiple_files = []
        for filename in report_files:
            with open(filename, 'rb') as input_file:
                data_obj = io.BytesIO(input_file.read())
                multiple_files.append(('report', (os.path.basename(filename), data_obj)))
        return self.post(
            f"{self._api_url_version}/projects/{self.project}/external-analysis/session/auto-create/report",
            params={
                "t": self._get_timestamp_parameter(timestamp),
                "message": message,
                "partition": partition,
                "format": report_format.value,
                "movetolastcommit": move_to_last_commit
            },
            files=multiple_files,
            headers={"Content-Type": "multipart/form-data"}
        )

    def upload_architectures(
            self, architectures: Dict, timestamp: datetime.datetime, message: str,
            architecture_format: ArchitectureFormats = ArchitectureFormats.FILE_LIST
    ) -> requests.Response:
        """Upload architectures to Teamscale. It is expected that the given architectures can
        be read from the filesystem.

        Args:
            architectures: mapping of teamscale paths to architecture files that should be uploaded.
                Files must be readable.
            timestamp: timestamp for which to upload the data
            message: The message to use for the generated upload commit
            architecture_format: the architecture file format

        Returns:
            requests.Response: object generated by the request

        Raises:
            ServiceError: If anything goes wrong
        """
        architecture_files = [(path, open(filename, 'rb')) for path, filename in architectures.items()]
        return self.post(
            f"{self._api_url_version}/projects/{self.project}/architectures",
            params={
                "t": self._get_timestamp_parameter(timestamp),
                "message": message,
                "format": architecture_format.value
            },
            files=architecture_files,
            headers={"Content-Type": "multipart/form-data"}
        )

    def upload_non_code_metrics(
            self, metrics: List[NonCodeMetricEntry], timestamp: datetime.datetime, message: str, partition: str
    ) -> requests.Response:
        """Uploads a list of non-code metrics

        Args:
            metrics: metrics data
            timestamp: timestamp for which to upload the metrics
            message: The message to use for the generated upload commit
            partition: The partition's id into which the metrics should be added
                (See also: :ref:`FAQ - Partitions<faq-partition>`).

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self._upload_external_data("non-code-metrics", to_json(metrics), timestamp, message, partition)

    def get_baselines(self) -> List[Baseline]:
        """Retrieves a list of baselines from the server for the currently active project.

        Returns:
            List[:class:`data.Baseline`]): The list of baselines.

        Raises:
            ServiceError: If anything goes wrong
        """
        response = self.get(f"{self._api_url_version}/projects/{self.project}/baselines")
        return [Baseline.from_json(json_data) for json_data in response.json()]

    def delete_baseline(self, baseline_name: str) -> requests.Response:
        """Deletes a baseline from the currently active project.

        Args:
            baseline_name: The baseline that is to be removed.

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.delete(f"{self._api_url_version}/projects/{self.project}/baselines/baselines/{baseline_name}")

    def add_baseline(self, baseline: Baseline) -> requests.Response:
        """Adds a baseline to the currently active project.
        Re-adding an existing baseline will update the original baseline.

        Args:
            baseline: The baseline that is to be added (or updated)

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            ServiceError: If anything goes wrong
        """
        return self.put(
            f"{self._api_url_version}/projects/{self.project}/baselines/baselines/{baseline.name}",
            data=to_json(baseline)
        )

    def get_projects(self) -> List[ProjectInfo]:
        """Retrieves a list of projects from the server.

        Returns:
            List[:class:`data.ProjectInfo`]): The list of projects.

        Raises:
            ServiceError: If anything goes wrong
        """
        response = self.get(
            f"{self._api_url_version}/projects",
            parameters={
                "include-deleting": True,
                "include-reanalyzing": True
            }
        )
        return [ProjectInfo.from_json(json_data) for json_data in response.json()]

    def create_project(
            self, project_configuration: ProjectConfiguration, skip_project_validation: bool = False
    ) -> requests.Response:
        """Creates a project with the specified configuration in Teamscale. The parameter `skip_project_validation`
        specifies, whether to skip the validation of the project.

        Args:
            project_configuration: The configuration for the project to be created.
            skip_project_validation: Whether to skip validation of the project.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self.post(
            f"{self._api_url_version}/projects",
            params={
                "skip-project-validation": skip_project_validation,
                "reanalyze-if-required": True
            },
            data=to_json(project_configuration)
        )

    def update_project(
            self, project_configuration: ProjectConfiguration, skip_project_validation: bool = False
    ) -> requests.Response:
        """Updates an existing project in Teamscale with the given configuration. This may trigger a reanalysis of the
         project if the changes require it. The id of the existing project is taken from the configuration.
         The parameter `skip_project_validation` specifies, whether to skip the validation of the project.

        Args:
            project_configuration: The configuration for the project to be updated.
            skip_project_validation: Whether to skip validation of the project.
        Returns:
            requests.Response: object generated by the upload request.

        Raises:
            ServiceError: If anything goes wrong.
        """
        return self.put(
            f"{self._api_url_version}/projects/{project_configuration.id}",
            params={
                "skip-project-validation": skip_project_validation,
                "reanalyze-if-required": True
            },
            data=to_json(project_configuration)
        )

    def _get_timestamp_parameter(self, timestamp: datetime.datetime, branch: Optional[str] = None) -> str:
        """Returns the timestamp parameter. Will use the branch parameter if it is set.
        Returned timestamp is 'HEAD' if given timestamp is `None`.

        Args:
            timestamp: The timestamp to convert
            branch: The branch to use. If this parameter is not set, the branch that was used to initialize the
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

    @classmethod
    def read_json_from_file(cls, file_path: str) -> Any:
        """Reads JSON content from a file and parses it to ensure basic integrity.

        Args:
            file_path: File from which to read the JSON content.

        Returns:
            The parsed JSON data.
        """
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data

    def upload_files_for_precommit_analysis(
            self, timestamp: datetime.datetime, precommit_data: Dict) -> requests.Response:
        """Uploads the provided files for precommit analysis.

        Args:
            timestamp: The timestamp of the parent commit.
            precommit_data: The content and paths of added, modified and removed files. The dictionary should contain
                a key "deletedUniformPaths" mapping to str and "uniformPathToContentMap" mapping to an object
        """
        return self.post(
            f"{self._api_url_version}/projects/{self.project}/pre-commit/{self._get_timestamp_parameter(timestamp)}",
            json=precommit_data
        )

    def get_precommit_analysis_results(self) -> Tuple[List[Finding], ...]:
        """Gets precommit analysis results.

        Returns:
            A tuple consisting of three lists: added findings, findings in changed code, and removed findings.
        """
        service_url = f"{self._api_url_version}/projects/{self.project}/pre-commit"

        while True:
            response = self.get(service_url)
            # We need to wait for 200 here to get the findings.
            # The service returns 204 while the pre-commit analysis is still in progress.
            if response.status_code != 204:
                time.sleep(2)
            elif response.status_code == 200:
                json_data = response.json()
                return tuple(map(
                    lambda category: [Finding.from_json(json_findings) for json_findings in json_data[category]],
                    ["addedFindings", "findingsInChangedCode", "removedFindings"]
                ))
            else:
                raise ServiceError(f"ERROR: GET {service_url}: {response.status_code}:{response.text}")

    def get_findings(
            self, uniform_path: str, timestamp: datetime.datetime, revision_id: Optional[str] = None,
            filter: Optional[FileFindings] = None, invert: bool = False,
            assessment_filters: Optional[List[Assessment]] = None
    ) -> List[Finding]:
        """Retrieves the list of findings in the currently active project for the given uniform path
        at the provided timestamp on the given branch.

        Args:
            uniform_path: The uniform path to get findings for.
            timestamp: timestamp (unix format) for which to upload the data
            revision_id: If provided, the client will first resolve the ID (e.g., commit hash) to a Teamscale
               commit and retrieve the findings for the corresponding branch.
            filter: The finding category, group, and type filters. 
                Every string must be either a single category, a combination category/group, or a type ID. 
                If a category or group is given, all matching findings
                will be filtered out and not included in the result.
            invert: Whether to invert the category, group, type filters, 
                i.e. including the elements given in the filters instead of excluding them.
            assessment_filters: The assessment filter. All mentioned assessment colors
                will be filtered out and not included in the result.

        Returns:
            List[:class:`data.Finding`]): The list of findings.

        Raises:
            ServiceError: If anything goes wrong
        """
        if revision_id:
            timestamp = self.get_commit_for_revision(revision_id)
        else:
            timestamp = self._get_timestamp_parameter(timestamp=timestamp)

        parameters = {
            "t": timestamp,
            "invert": invert,
            "uniform-path": uniform_path,
            "all": True
        }
        if filter:
            parameters["filter"] = filter
        if assessment_filters:
            parameters["assessment-filters"] = list(map(lambda assessment: assessment.value, assessment_filters))

        service_url = f"{self._api_url_version}/projects/{self.project}/findings/list"
        response = self.get(service_url, parameters)
        return [Finding.from_json(json_data) for json_data in response.json()]

    def get_commit_for_revision(self, revision_id: str) -> str:
        """Retrieves the Teamscale commit corresponding to a revision, raising an error if the commit is not known
        to Teamscale.

        Args:
            revision_id: The revision ID (e.g., commit SHA)

        Returns:
            str: The teamscale commit
        """
        response = self.get(f"{self._api_url_version}/projects/{self.project}/revision/{revision_id}/commits")
        commit_list = response.json()

        if not commit_list:
            raise ServiceError(f"Could not find commit in Teamscale for given revision: {revision_id}")

        return commit_list[0]["branchName"] + ":" + str(commit_list[0]["timestamp"])

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
        service_url = f"{self._api_url_version}/projects/{self.project}/findings/{finding_id}"
        response = self.get(
            service_url,
            parameters={
                "t": self._get_timestamp_parameter(timestamp=timestamp, branch=branch)
            }
        )
        return Finding.from_json(response.json())

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
        parameters = {"status": status, "details": details, "start": start, "max": max, "with-count": False}
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
        return requests.post(service_url, auth=self.auth_header, verify=self.sslverify, files=multiple_files,
                             timeout=self.timeout)

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
        parameters = {"list": True,

                      }
        response = self.get(service_url, parameters=parameters)
        if not response.ok:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=service_url, r=response))
        return [architecture_overview['uniformPath'] for architecture_overview in response.json()]
