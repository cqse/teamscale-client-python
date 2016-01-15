import requests
import responses
from teamscale_client import TeamscaleClient

def get_client():
    return TeamscaleClient("http://localhost:8080", "admin", "admin", "foo")

@responses.activate
def test_put():
    responses.add(responses.PUT, 'http://localhost:8080',
                      body='success', status=200)
    resp = get_client().put("http://localhost:8080", "[]", {})
    assert resp.text == "success"
