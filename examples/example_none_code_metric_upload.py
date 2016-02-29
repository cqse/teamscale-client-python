from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import AssessmentMetricColors
from teamscale_client.data import NoneCodeMetricEntry, NoneCodeMetrics


TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
PASSWORD = "admin"

PROJECT_NAME = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)

    entry = NoneCodeMetricEntry("/none/code/metric/path", NoneCodeMetrics("This is a test content", {AssessmentMetricColors.RED: 2, AssessmentMetricColors.GREEN : 1}, 25.0))
    entry2 = NoneCodeMetricEntry("/none/code/metric/path2", NoneCodeMetrics("This is a test content 2", {AssessmentMetricColors.RED: 1, AssessmentMetricColors.GREEN : 4}, 40.))

    client.upload_none_code_metrics([entry, entry2], datetime.datetime.now() , "Upload none-code metrics", "test-partition")
