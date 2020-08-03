from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import os

import openapi_client

from openapi_client.exceptions import ApiException
from util.teamscale_utils import get_timestamp_parameter

TEAMSCALE_URL = 'http://localhost:8080'
USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-key'
PROJECT_ID = 'junit4'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)

with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ArchitectureApi(api_client)
    try:
        architecture_files = []
        for root, dirs, files in os.walk(r'/path/to/architectures'):
            for file in files:
                architecture_files.append(os.path.join(os.path.abspath(root), file))
        print(architecture_files)
        client.upload_architecture(PROJECT_ID, file=architecture_files,
                                   t=get_timestamp_parameter(datetime.datetime.now()), message='Upload architecture')
    except ApiException as e:
        print('Exception when calling ArchitectureApi->upload_architectures: %s\n' % e)
