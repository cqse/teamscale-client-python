import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.data import MetricEntry

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "foo"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    entry = MetricEntry("src/Foo.java", {"sample_metric_id": 10})
    entry2 = MetricEntry("-architectures-/system.architecture/src/empty/", {"sample_metric_id": 6})

    client.upload_metrics([entry2], datetime.datetime.now(), "Upload metrics", "test-partition")
