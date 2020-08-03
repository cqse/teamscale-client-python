from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import openapi_client

from openapi_client.models import NonCodeMetricsEntry
from openapi_client.exceptions import ApiException
from util.constants import AssessmentMetricColors
from util.teamscale_utils import get_timestamp_parameter

TEAMSCALE_URL = 'http://localhost:8080'
USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-token'
PROJECT_ID = 'test'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)

with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ExternalAnalysisApi(api_client)

    try:
        entry = NonCodeMetricsEntry("/non/code/metric/path", "This is a test content", 25.0, 3,
                                    {AssessmentMetricColors.RED: 2, AssessmentMetricColors.GREEN: 1})
        entry2 = NonCodeMetricsEntry("/non/code/metric/path2", "This is a test content 2", 40., 5,
                                     {AssessmentMetricColors.RED: 1, AssessmentMetricColors.GREEN: 4})
        client.upload_non_code_metrics(PROJECT_ID, 'auto-create', [entry, entry2],
                                       t=get_timestamp_parameter(datetime.datetime.now()),
                                       message='Upload non-code metrics',
                                       partition='test-partition')
    except ApiException as e:
        print('Exception when calling ExternalAnalysisApi: %s\n' % e)
