# This script uploads all coverage under the given folder to Teamscale. Folder structure:
# - root_folder
#   - project_id
#     - filename.coverage_format
# This will upload the coverage in filename.coverage_format to the project with the ID project_id as coverage of the format coverage_format.
# The file name may be arbitrary.
# The coverage files are deleted after a successful upload.
# You can run this script, e.g. in a cron job and have your build drop coverage files in the root_folder

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests

import datetime
import os
import sys

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "build"
ACCESS_TOKEN = "access_token"
    
def main(coverage_folder):
    print("\n---> checking for new coverage at %s" % datetime.datetime.now())
    projects = [f for f in os.listdir(coverage_folder) if os.path.isdir(os.path.join(coverage_folder, f))]
    for project in projects:
        project_path = os.path.join(coverage_folder, project)
        client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, project)
        coverage_files = [f for f in os.listdir(project_path) if os.path.isfile(os.path.join(project_path, f))]
        for coverage_file in coverage_files:
            coverage_path = os.path.join(project_path, coverage_file)
            format = os.path.splitext(coverage_file)[1]
            print("uploading coverage to %s from %s" % (project, coverage_file))
            client.upload_coverage_data([coverage_path], format, datetime.datetime.now(), "Unit Test Coverage Upload", "Unit Test Coverage")
            os.remove(coverage_path)

if __name__ == '__main__':
    main(sys.argv[1])

    
