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
PASSWORD = "F0VzQ_2Q2wqGmBFBrI6EIVWVK4QxR55o"

PROJECT_NAME = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)

    client.upload_architectures({"archs/abap.architecture": "/home/kinnen/repos/conqat-cqse_bmw/engine/eu.cqse.conqat.engine.abap/abap_exporter.architecture"}, datetime.datetime.now(), "Upload architecture")
