from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from datetime import datetime

import openapi_client
from util.constants import ReportFormats
from openapi_client.exceptions import ApiException
from util.teamscale_utils import get_timestamp_parameter

TEAMSCALE_URL = 'http://localhost:8080'
USERNAME = 'user'
ACCESS_KEY = 'ide-access-key'
PROJECT_ID = 'test-project'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_KEY
)


with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ExternalAnalysisApi(api_client)
    reports = []
    for root, dirs, files in os.walk(r'/path/to/reports'):
        for file in files:
            reports.append(os.path.join(os.path.abspath(root), file))
    try:
        client.upload_report(PROJECT_ID, 'auto-create', ReportFormats.PYLINT,
                             t=get_timestamp_parameter(datetime.now()),
                             message='Upload PyLint results',
                             partition='test-partition', report=reports)
    except ApiException as e:
        print('Exception when calling ExternalAnalysisApi->upload_report: %s\n' % e)
