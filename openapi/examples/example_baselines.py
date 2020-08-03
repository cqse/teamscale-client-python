from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models import BaselineInfo
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


def show_baselines():
    baselines = client.get_all_baselines(PROJECT_ID)
    print([str(baseline) for baseline in baselines])


with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.BaselinesApi(api_client)
    try:
        newBaseline = BaselineInfo('Test Baseline', 'This is a test description',
                                   get_timestamp_parameter(datetime.datetime.now()))
        client.create_or_update_baseline(PROJECT_ID, newBaseline.name, newBaseline)
        show_baselines()

        newBaseline = BaselineInfo('Test Baseline', 'This is a test description',
                                   get_timestamp_parameter(datetime.datetime.now()))
        client.create_or_update_baseline(PROJECT_ID, newBaseline.name, newBaseline)

        newBaseline2 = BaselineInfo('Test Baseline 2', 'This is a test description',
                                    get_timestamp_parameter(datetime.datetime.now()))
        client.create_or_update_baseline(PROJECT_ID, newBaseline2.name, newBaseline2)
        show_baselines()

        client.delete_baseline(PROJECT_ID, newBaseline2.name)
        show_baselines()

    except ApiException as e:
        print('Exception when calling BaselinesApi: %s\n' % e)
