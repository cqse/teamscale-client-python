from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models import ExternalMetricsEntry
from util.teamscale_utils import get_timestamp_parameter

TEAMSCALE_URL = 'http://localhost:8080'

USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-key'
PROJECT_ID = 'test'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)

with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ExternalMetricsApi(api_client)

    try:
        entry = ExternalMetricsEntry('second.c', {'sample_metric_id': 10})
        entry2 = ExternalMetricsEntry('-architectures-/system.architecture/src/empty/', {'sample_metric_id': 6})

        client.upload_external_metrics(PROJECT_ID, 'auto-create', [entry, entry2],
                                       t=get_timestamp_parameter(datetime.datetime.now()), message='Upload metrics',
                                       partition='test-partition')

    except ApiException as e:
        print('Exception when calling ExternalMetricsApi: %s\n' % e)
