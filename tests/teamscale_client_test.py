import requests
import responses
import re
from teamscale_client.teamscale_client import TeamscaleClient

URL = "http://localhost:8080"

def get_client():
    return TeamscaleClient(URL, "admin", "admin", "foo")

def get_project_service_mock(service_id):
    return re.compile(r'%s/p/foo/%s/.*' % (URL, service_id))

def get_global_service_mock(service_id):
    return re.compile(r'%s/%s/.*' % (URL, service_id))

@responses.activate
def test_put():
    responses.add(responses.PUT, 'http://localhost:8080',
                      body='success', status=200)
    resp = get_client().put("http://localhost:8080", "[]", {})
    assert resp.text == "success"

@responses.activate
def test_upload_findings():
    responses.add(responses.PUT, get_project_service_mock('add-external-findings'),
                      body='success', status=200)
    resp = get_client().upload_findings([], 18073649127634, "Test message", "partition-name")
    assert resp.text == "success"

@responses.activate
def test_upload_metrics():
    responses.add(responses.PUT, get_project_service_mock('add-external-metrics'),
                      body='success', status=200)
    resp = get_client().upload_metrics([], 18073649127634, "Test message", "partition-name")
    assert resp.text == "success"

@responses.activate
def test_upload_metric_description():
    responses.add(responses.PUT, get_global_service_mock('add-external-metric-description'),
                      body='success', status=200)
    resp = get_client().upload_metric_definitions([])
    assert resp.text == "success"

