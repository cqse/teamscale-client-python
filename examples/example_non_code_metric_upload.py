import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import AssessmentMetricColors
from teamscale_client.data import NonCodeMetricEntry

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    entry = NonCodeMetricEntry("/non/code/metric/path", "This is a test content", 3,
                               {AssessmentMetricColors.RED: 2, AssessmentMetricColors.GREEN: 1}, 25.0)
    entry2 = NonCodeMetricEntry("/non/code/metric/path2", "This is a test content 2", 5,
                                {AssessmentMetricColors.RED: 1, AssessmentMetricColors.GREEN: 4}, 40.)

    client.upload_non_code_metrics(
        [entry, entry2], "Upload non-code metrics", "test-partition", timestamp=datetime.datetime.now()
    )
