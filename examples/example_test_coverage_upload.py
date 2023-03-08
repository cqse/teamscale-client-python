import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import CoverageFormats

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "junit4"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    files = ["./simple-coverage.txt"]

    client.upload_coverage_data(
        files, CoverageFormats.SIMPLE, "Upload coverage", "test-partition", timestamp=datetime.datetime.now()
    )
