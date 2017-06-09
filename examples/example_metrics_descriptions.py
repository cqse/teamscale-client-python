from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from teamscale_client import TeamscaleClient
from teamscale_client.data import MetricDescription

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "foo"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    description = MetricDescription("sample_metric_id", "Sample Metric", "A great sample description", "Sample Metrics")
    client.add_metric_descriptions([description])
