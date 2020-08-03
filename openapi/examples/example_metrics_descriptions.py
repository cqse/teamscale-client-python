from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models import MetricSchemaChangeEntry
from openapi_client.models import MetricDirectorySchemaEntry

from util.constants import MetricAggregation
from util.constants import MetricValueType
from util.constants import MetricProperties

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
        description = MetricSchemaChangeEntry('sample_metric_id', 'Sample Metrics',
                                              MetricDirectorySchemaEntry('Sample Metric', 'A great sample description',
                                                                         aggregation=MetricAggregation.SUM,
                                                                         value_type=MetricValueType.NUMERIC,
                                                                         properties=(MetricProperties.SIZE_METRIC,)))
        client.add_external_metrics([description])

    except ApiException as e:
        print('Exception when calling ExternalMetricsApi: %s\n' % e)
