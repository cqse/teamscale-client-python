# This script uploads all coverage under the given folder to Teamscale. Folder structure:
# - root_folder
#   - project_id
#     - filename.coverage_format
# This will upload the coverage in filename.coverage_format to the project
# with the ID project_id as coverage of the format coverage_format.
# The file name may be arbitrary.
# The coverage files are deleted after a successful upload.
# You can run this script, e.g. in a cron job and have your build drop coverage files in the root_folder

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import os
import sys
import openapi_client

from util.teamscale_utils import get_timestamp_parameter
from openapi_client.exceptions import ApiException


TEAMSCALE_URL = 'http://localhost:8080'

USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-key'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)


with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ExternalAnalysisApi(api_client)
    coverage_folder = sys.argv[1]
    print('\n---> checking for new coverage at %s' % datetime.datetime.now())
    projects = [f for f in os.listdir(coverage_folder) if os.path.isdir(os.path.join(coverage_folder, f))]
    try:
        for project in projects:
            project_path = os.path.join(coverage_folder, project)
            coverage_files = [f for f in os.listdir(project_path) if os.path.isfile(os.path.join(project_path, f))]
            for coverage_file in coverage_files:
                coverage_path = os.path.join(project_path, coverage_file)
                coverageFormat = os.path.splitext(coverage_file)[1][1:]
                print('uploading coverage to %s from %s' % (project, coverage_file))
                print(coverageFormat)
                client.upload_report(project, 'auto-create', report=[coverage_path], format=coverageFormat,
                                     t=get_timestamp_parameter(datetime.datetime.now()),
                                     message='Unit Test Coverage Upload',
                                     partition='Unit Test Coverage')
                os.remove(coverage_path)
    except ApiException as e:
        print('Exception when calling ExternalAnalysisApi: %s\n' % e)
