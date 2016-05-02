from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
PASSWORD = "admin"

PROJECT_NAME = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)

    client.upload_architectures({"architectures/system.architecture": "/home/user/a/path/to/system.architecture"}, datetime.datetime.now(), "Upload architecture", "test-partition")
