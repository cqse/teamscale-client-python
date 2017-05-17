from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import ReportFormats

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_NAME = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_NAME)

    files = [ file for file in glob.glob("/path/to/report.xml")]

    client.upload_report(files, ReportFormats.PCLINT , datetime.datetime.now(), "Upload PCLint results", "test-partition")
