"""All tests mocked using the responses api:

https://github.com/getsentry/responses
"""
import datetime

import responses

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats, AssessmentMetricColors, Enablement, TaskStatus
from teamscale_client.data import Finding, FileFindings, MetricDescription, MetricEntry, NonCodeMetricEntry, Baseline, \
    FileSystemSourceCodeConnectorConfiguration, ProjectConfiguration, FindingDescription
from teamscale_client.utils import to_json

TEAMSCALE_TEST_VERSION = "v8.0.0"
PROJECT = "foo"
USER = "admin"
ACCESS_TOKEN = USER

BASE_URL = "http://localhost:8080"
BASE_API_URL = f"{BASE_URL}/api"
BASE_API_VERSIONED_URL = f"{BASE_API_URL}/{TEAMSCALE_TEST_VERSION}"


def get_client(branch=None):
    """Returns Teamscale client object for requesting servers"""
    responses.add(
        responses.GET, f"{BASE_API_URL}/version", status=200, content_type="application/json", json={
            "maxApiVersion": {
                "major": 8,
                "minor": 6,
                "patch": 5
            },
            "minApiVersion": {
                "major": 5,
                "minor": 7,
                "patch": 0
            }
        }
    )
    return TeamscaleClient(BASE_URL, USER, ACCESS_TOKEN, PROJECT, branch=branch)


@responses.activate
def test_client_creation():
    """Test that a client is created with the requested parameters and ensures that at least one test fails if the
    version number changes"""
    assert TeamscaleClient.TEAMSCALE_API_VERSION == TEAMSCALE_TEST_VERSION
    client = get_client()
    assert client.url == BASE_URL
    assert client.project == PROJECT
    assert client.username == USER


@responses.activate
def test_put():
    """Tests PUT requests to server"""
    responses.add(responses.PUT, BASE_URL, status=200)
    resp = get_client().put(BASE_URL)
    assert resp.ok


@responses.activate
def test_add_findings_group():
    """ Tests uploading of findings groups into Teamscale server.
    """
    responses.add(responses.POST, f"{BASE_API_VERSIONED_URL}/external-findings/groups", status=200)
    resp = get_client().add_findings_group('name', 'map.*')
    assert resp.ok


@responses.activate
def test_add_findings_descriptions():
    """ Tests uploading of findings descriptions into Teamscale server
    """
    findings_descriptions = [FindingDescription('type1', 'desc1', Enablement.RED, 'name1'),
                             FindingDescription('type2', 'desc2', Enablement.YELLOW, 'name 2')]
    responses.add(responses.POST, f"{BASE_API_VERSIONED_URL}/external-findings/descriptions", status=200)
    resp = get_client().add_finding_descriptions(findings_descriptions)
    assert resp.ok


@responses.activate
def test_upload_findings():
    """Tests uploading of findings"""
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/external-analysis/session/auto-create/external-findings",
        status=200
    )
    resp = get_client().upload_findings(_get_test_findings(), "Test message", "partition-name",
                                        timestamp=datetime.datetime.now())
    assert "content" in responses.calls[1].request.body
    assert "test-id" in responses.calls[1].request.body
    assert resp.ok


@responses.activate
def test_upload_metrics():
    """Tests uploading of metrics"""
    metric = MetricEntry("test/path", {"metric-1": 1, "metric-2": [1, 3, 4]})
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/external-analysis/session/auto-create/external-metrics",
        status=200
    )
    resp = get_client().upload_metrics([metric], "Test message", "partition-name", timestamp=datetime.datetime.now())
    assert '[{"metrics": {"metric-1": 1, "metric-2": [1, 3, 4]}, "path": "test/path"}]' == \
           responses.calls[1].request.body
    assert resp.ok


@responses.activate
def test_upload_non_code_metrics():
    """Tests uploading of non code metrics"""
    metric = NonCodeMetricEntry("metric1/non/code/metric/path", "This is a test content", 2,
                                {AssessmentMetricColors.RED: 2, AssessmentMetricColors.GREEN: 1}, 25.0)
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/external-analysis/session/auto-create/non-code-metrics",
        status=200
    )
    resp = get_client().upload_non_code_metrics(
        [metric], "Test message", "partition-name", timestamp=datetime.datetime.now()
    )
    assert '[{"assessment": {"GREEN": 1, "RED": 2}, "content": "This is a test content", "count": 2, ' \
           '"path": "metric1/non/code/metric/path", "time": 25.0}]' == \
           responses.calls[1].request.body
    assert resp.ok


@responses.activate
def test_upload_metric_description():
    """Tests uploading of metric descriptions"""
    description = MetricDescription("metric_i,", "Metric Name", "Great Description", "awesome group")
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/external-metrics",
        status=200
    )
    resp = get_client().add_metric_descriptions([description])
    assert '{"analysisGroup": "awesome group", "metricDefinition": {"aggregation": "SUM", "description": "Great ' \
           'Description", "name": "Metric Name", "properties": ["SIZE_METRIC"], "valueType": "NUMERIC"}, "metricId": ' \
           '"metric_i,"}' == to_json(description)
    assert resp.ok


@responses.activate
def test_coverage_upload():
    """Tests uploading of test coverage"""
    files = ["tests/data/file1.txt", "tests/data/file2.txt"]
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/external-analysis/session/auto-create/report",
        status=200
    )
    resp = get_client().upload_coverage_data(files, CoverageFormats.CTC, "Test Message",
                                             "partition-name", timestamp=datetime.datetime.now())
    assert resp.ok
    assert "file1.txt" in responses.calls[1].request.body.decode()
    assert "file2.txt" in responses.calls[1].request.body.decode()


@responses.activate
def test_get_baseline():
    """Tests retrieving of baselines"""
    responses.add(responses.GET, f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/baselines",
                  status=200, content_type="application/json",
                  body='[{ "name": "Baseline 1", "description": "Test description", "timestamp": 123192873091 }]')
    resp = get_client().get_baselines()
    assert len(resp) == 1
    assert resp[0].name == "Baseline 1"


@responses.activate
def test_add_baseline():
    """Test uploading of baselines"""
    baseline = Baseline("Baseline 1", "Test description", datetime.datetime.now())
    responses.add(
        responses.PUT,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/baselines/{baseline.name}",
        status=200
    )
    resp = get_client().add_baseline(baseline)
    assert resp.ok
    assert "Baseline 1" in responses.calls[1].request.body


@responses.activate
def test_delete_baseline():
    """Test deletion of baselines"""
    baseline_name = "Baseline 1"
    responses.add(
        responses.DELETE,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/baselines/{baseline_name}",
        status=200
    )
    resp = get_client().delete_baseline(baseline_name)
    assert resp.ok


@responses.activate
def test_architecture_upload():
    """Tests uploading of architectures"""
    # Just reuse text files for testing, it's just a mock anyway
    paths = {"archs/first.architecture": "tests/data/file1.txt", "archs/second.architecture": "tests/data/file2.txt"}
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/architectures",
        status=200
    )
    resp = get_client().upload_architectures(paths, "Test Message", timestamp=datetime.datetime.now())
    assert resp.ok
    assert "file1.txt" in responses.calls[1].request.body.decode()
    assert "file2.txt" in responses.calls[1].request.body.decode()


def _get_test_findings():
    """Returns test findings"""
    finding = Finding("test-id", "message")
    return [FileFindings([finding], "path/to/file")]


def test_finding_json_serialization():
    """Tests that findings json is correctly serialized"""
    findings = _get_test_findings()
    assert '[{"content": null, "findings": [{"assessment": "YELLOW", "endLine": null, "endOffset": null, ' \
           '"findingProperties": null, "findingTypeId": "test-id", "finding_id": null, "identifier": null, ' \
           '"message": "message", "startLine": null, "startOffset": null, "uniformPath": null}], ' \
           '"path": "path/to/file"}]' == to_json(findings)


@responses.activate
def test_get_projects():
    """Tests retrieving of projects"""
    responses.add(
        responses.GET,
        f"{BASE_API_VERSIONED_URL}/projects",
        status=200, content_type="application/json",
        body='[{"description": "", "creationTimestamp": 1487534523817, "alias": "My Test Project", "reanalyzing": '
             'false, "deleting": false, "publicIds": ["test-project"], "internalId": "test-project", "name": "Test '
             'Project"}]')
    resp = get_client().get_projects()
    assert len(resp) == 1
    assert resp[0].name == "Test Project"


@responses.activate
def test_add_project():
    """Test adding projects"""
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory="/path/to/folder",
                                                                    repository_identifier="Local",
                                                                    included_file_names="**.py")
    project_configuration = ProjectConfiguration(name="Test Project", project_id="test-project",
                                                 profile="Python (default)", connectors=[file_system_config])
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects",
        body='{"message": "success"}', status=200
    )
    resp = get_client().create_project(project_configuration)
    assert resp.ok
    assert resp.json().get('message') == "success"


@responses.activate
def test_add_project_without_validation():
    """Test adding projects"""
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory="/path/to/folder",
                                                                    repository_identifier="Local",
                                                                    included_file_names="**.py")
    project_configuration = ProjectConfiguration(name="Test Project", project_id="test-project",
                                                 profile="Python (default)", connectors=[file_system_config])
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects",
        body='{"message": "success"}', status=200
    )
    resp = get_client().create_project(project_configuration, True)
    assert resp.ok
    assert resp.json().get('message') == "success"


def test_compare_findings():
    """Tests comparing between findings."""
    first_finding = Finding("1a", "first message a", uniform_path='path/to/a', start_line=10, end_line=30)
    second_finding = Finding("2", "second message", uniform_path='path/to/a', start_line=20, end_line=25)
    third_finding = Finding("3", "third message", uniform_path='path/to/b', start_line=20, end_line=25)
    assert first_finding < second_finding
    assert second_finding < third_finding
    assert first_finding == first_finding
    assert third_finding > second_finding
    assert second_finding >= first_finding
    assert second_finding >= first_finding
    assert second_finding != first_finding


@responses.activate
def test_get_tasks():
    """Tests retrieving of tasks"""
    responses.add(
        responses.GET,
        f"{BASE_API_URL}/projects/{PROJECT}/tasks",
        status=200, content_type="application/json",
        body='[{"id": 1, "subject": "uiae", "author": "admin", "description": "", "assignee": "", "created": '
             '1536581194732, "updated": 1536583991791, "updatedBy": "admin", "status": "OPEN", "resolution": "NONE", '
             '"findings": [{"findingId": "40315BE118FE08044FBF605325445250"}], "comments": [{"author": "admin", '
             '"date": 1536583991791, "text": "Added finding: 40315BE118FE08044FBF605325445250", "changeComment": '
             'true, "resolvedAuthor": {"username": "admin", "firstName": "Default", "lastName": "Administrator", '
             '"emailAddress": "", "gravatarHash": "dummy", "useGravatar": false, "aliases": [], "authenticator": '
             '"HashedStored:anonymized", "groupIds": ["Administrators"]}}], "tags": [], "resolvedAuthor": {'
             '"username": "admin", "firstName": "Default", "lastName": "Administrator", "emailAddress": "", '
             '"gravatarHash": "dummy", "useGravatar": false, "aliases": [], "authenticator": '
             '"HashedStored:anonymized", "groupIds": ["Administrators"]}, "resolvedUpdatedBy": {"username": "admin", '
             '"firstName": "Default", "lastName": "Administrator", "emailAddress": "", "gravatarHash": "dummy", '
             '"useGravatar": false, "aliases": [], "authenticator": "HashedStored:anonymized", "groupIds": ['
             '"Administrators"]}}]')
    resp = get_client().get_tasks(TaskStatus.OPEN)
    assert len(resp) == 1
    assert resp[0].id == 1
    assert resp[0].author == 'admin'


@responses.activate
def test_add_issue_metric():
    """Tests the addition of an issue metric"""
    responses.add(
        responses.POST,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/issues/queries",
        body='{"message": "success"}', status=200
    )
    resp = get_client().add_issue_metric("example/foo", "instate(status=YELLOW) > 2d")
    assert resp.ok
    assert "YELLOW" in responses.calls[1].request.params["query"]
    assert resp.json().get('message') == "success"


@responses.activate
def test_get_timestamp_parameter():
    """Tests that timestamp and branch are correctly handled when creating the timestamp parameter."""
    master_client = get_client('master')
    _assert_timestamp_parameter(master_client, None, 1, 'master:1000')
    _assert_timestamp_parameter(master_client, None, None, 'master:HEAD')
    _assert_timestamp_parameter(master_client, 'develop', 1, 'develop:1000')
    _assert_timestamp_parameter(master_client, 'develop', None, 'develop:HEAD')

    branchless_client = get_client()
    _assert_timestamp_parameter(branchless_client, None, 1, '1000')
    _assert_timestamp_parameter(branchless_client, None, None, 'HEAD')
    _assert_timestamp_parameter(branchless_client, 'develop', 1, 'develop:1000')
    _assert_timestamp_parameter(branchless_client, 'develop', None, 'develop:HEAD')


def _assert_timestamp_parameter(client, branch, timestamp, expected_parameter):
    given_timestamp = datetime.datetime.fromtimestamp(timestamp) if timestamp else None
    timestamp_parameter = client._get_timestamp_parameter(given_timestamp, branch)
    assert timestamp_parameter == expected_parameter


@responses.activate
def test_get_finding_by_id():
    """Tests retrieving findings by id."""
    finding_id = '1A1837926D5406B9B33DDB84A1383525'
    uniformPath = 'teamscale_client/client.py'
    startLine = 450
    endLine = 450
    startOffset = 19808
    endOffset = 19828
    findingTypeId = 'Code Anomalies/Assignment of a variable to itself'
    message = '`parameters` is assigned to itself'
    assessment = AssessmentMetricColors.YELLOW
    finding_properties = {
        "Check": "Assignment of a variable to itself"
    }

    responses.add(
        responses.GET,
        f"{BASE_API_VERSIONED_URL}/projects/{PROJECT}/findings/{finding_id}",
        status=200, content_type="application/json",
        body=(f'{{"typeId": "{findingTypeId}", "categoryName": "Code Anomalies", "analysisTimestamp": -1, '
              f'"groupName": "Bad practice", "location": {{"rawStartOffset": {startOffset}, "@class": '
              f'"org.conqat.engine.commons.findings.location.TextRegionLocation", "rawEndLine": {endLine}, '
              f'"rawEndOffset": {endOffset}, "location": "{uniformPath}", "rawStartLine": {startLine}, '
              f'"uniformPath": "{uniformPath}"}}, "birth": {{"timestamp": 1487577242000,'
              f'"branchName": "master"}}, "id": "{finding_id}", "message": "{message}", '
              f'"assessment": "{assessment.value}", "properties": {to_json(finding_properties)}}}'
              )
    )
    finding = get_client().get_finding_by_id(finding_id)
    assert finding.uniformPath == uniformPath
    assert finding.startLine == startLine
    assert finding.endLine == endLine
    assert finding.startOffset == startOffset
    assert finding.endOffset == endOffset
    assert finding.findingTypeId == findingTypeId
    assert finding.message == message
    assert finding.assessment == assessment
    assert finding.identifier is None
    assert finding.findingProperties == finding_properties
