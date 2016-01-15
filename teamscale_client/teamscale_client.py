import collections
import requests
import simplejson as json
import time
from requests.auth import HTTPBasicAuth

FindingDescription = collections.namedtuple('FindingDescriptions', ['typeid', 'description', 'enablement'])
"""Description of finding to be added at configuration time."""


class ServiceError(Exception):
    """Teamscale service returned an error."""
    pass


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
    """

    def __init__(self, url, username, password, project, sslverify=True):
        self.url = url
        self.username = username
        self.auth_header = HTTPBasicAuth(username, password)
        self.project = project
        self.sslverify = sslverify

    def get(self, url, parameters=None):
        """Sends a get request to the given service url.

        Args:
            url (str):  The URL for which to execute a PUT request
            parameters (dict): parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        response = requests.get(url, params=parameters, auth=self.auth_header, verify=self.sslverify)
        if response.status_code != 200:
            raise ServiceError("ERROR: GET {url}: {r.status_code}:{r.text}".format(url=url, r=response))
        return response

    def put(self, url, jsontext, parameters=None):
        """Sends a put request to the given service url with the json payload as content.

        Args:
            url (str):  The URL for which to execute a PUT request
            jsontext: The JSON Object to attach as content
            parameters (dict): parameters to attach to the url

        Returns:
            requests.Response: request's response

        Raises:
            ServiceError: If anything goes wrong
        """
        response = requests.put(url, params=parameters, json=jsontext, headers={'Content-Type': 'application/json'}, auth=self.auth_header, verify=self.sslverify)
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
        url = self.get_global_service_url('add-external-findings-group')
        payload = [{'groupName': name, 'mapping': mapping_pattern}]
        return self.put(url, payload)

    def add_finding_descriptions(self, descriptions):
        """Adds descriptions of findings.

        Args:
            descriptions (list): List of ``FindingDescription`` to add to Teamscale.
        Returns:
            requests.Response: request's response
        """

        url = self.get_global_service_url('add-external-finding-descriptions')
        payload = [{'typeId': d.typeid, 'description': d.description, 'enablement': d.enablement} for d in descriptions]
        response = self.put(url, payload)

    def update_findings_schema(self):
        """Triggers refresh of finding groups in analysis profiles."""
        url = self.get_global_service_url('update-findings-schema')
        return self.get(url, {'projects': self.project})

    def upload_findings(self, findings, timestamp, message, partition):
        """Uploads a list of findings

        Args:
            findings: findings data in json format.
                The findings should have the following format::

                    [
                        {
                            "findings": [
                                {
                                    "findingTypeId" : "<external-finding-type-id>",
                                    "message" : "<findings message>",
                                    "assessment" : RED/YELLOW,
                                    "startLine" : 1,
                                    "endLine" : 1,
                                    "startOffset" : 1,
                                    "endOffset" : 26
                                }
                            ],
                            "path" : "path/to/file/in/teamscale"
                        },
                        ...
                    ]
            timestamp (datetime.datetime): timestamp for which to upload the findings
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the findings should be added

        Returns:
            requests.Response: object generated by the request

        Raises:
            Exception: If anything goes wrong
        """
        return self._upload_external_data("add-external-findings", findings, timestamp, message, partition)

    def upload_metrics(self, metrics, timestamp, message, partition):
        """Uploads a list of metrics

        Args:
            metrics: metrics data in json format.
                The metrics should have the following format::

                    [
                        {
                            "metrics": {
                                "<metric-id-1>": <metric-value>,
                                "<metric-id-2>": <metric-value>
                            },
                            "path": "path/to/file/in/teamscale"
                        },
                        ...
                    ]
            timestamp (datetime.datetime): timestamp for which to upload the metrics
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the metrics should be added

        Returns:
            requests.Response: object generated by the upload request

        Raises:
            Exception: If anything goes wrong
        """
        return self._upload_external_data("add-external-metrics", metrics, timestamp, message, partition)

    def _upload_external_data(self, service_name, json_data, timestamp, message, partition):
        """Uploads externals data in json format

        Args:
            service_name (str): The service name to which to upload the data
            json_data: data in json format
            timestamp (datetime.datetime): timestamp (unix format) for which to upload the data
            message (str): The message to use for the generated upload commit
            partition (str): The partition's id into which the data should be added

        Returns:
            requests.Response: object generated by the request

        Raises:
            Exception: If anything goes wrong
        """
        service_url = self.get_project_service_url(service_name)
        timestamp_seconds = time.mktime(timestamp.timetuple())
        parameters = {
            "t": int(timestamp_seconds * 1000),
            "message": message,
            "partition": partition,
            "skip-session": "true"
        }
        return self.put(service_url, json_data, parameters)

    def upload_metric_definitions(self, metric_definitions):
        """Uploads metric definitions in json format

        Args:
            metric_definitions: metric descriptions in json format
                The definitions should have the following format::

                    [
                        {
                            "analysisGroup": "<GROUP-NAME>",
                            "metricDefinition": {
                                "aggregation": "SUM",
                                "description": "-- not set --",
                                "name": "Sample Metric",
                                "properties": [
                                    "SIZE_METRIC"
                                ],
                                "valueType": "NUMERIC"
                            },
                            "metricId": "sample-metric-id"
                        },
                        ...
                    ]

        Returns:
            requests.Response: object generated by the request

        Raises:
            Exception: If anything goes wrong
        """
        service_url = self.get_global_service_url("add-external-metric-description")
        parameters = {}
        return self.put(service_url, metric_definitions, parameters)

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
