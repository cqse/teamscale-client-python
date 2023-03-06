import datetime
import glob

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    files = [file for file in glob.glob("/path/to/coverage/files/*.xml")]

    client.upload_coverage_data(files, CoverageFormats.CTC, datetime.datetime.now(), "Upload coverage",
                                "test-partition")
