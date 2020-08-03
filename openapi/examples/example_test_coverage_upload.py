from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import datetime
import openapi_client

from openapi_client.exceptions import ApiException
from util.constants import CoverageFormats
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
    client = openapi_client.ExternalAnalysisApi(api_client)
    try:
        files = [file for file in glob.glob('/path/to/coverage/files/*.xml')]
        client.upload_report(PROJECT_ID, 'auto-create', report=files, format=CoverageFormats.CTC,
                             t=get_timestamp_parameter(datetime.datetime.now()),
                             message='Upload coverage',
                             partition='test-partition')
    except ApiException as e:
        print('Exception when calling ExternalAnalysisApi->upload_report: %s\n' % e)
