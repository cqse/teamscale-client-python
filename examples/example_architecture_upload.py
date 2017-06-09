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
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    client.upload_architectures({"architectures/system.architecture": "/path/to/system.architecture"}, datetime.datetime.now(), "Upload architecture")
