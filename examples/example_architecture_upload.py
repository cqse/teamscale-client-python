import datetime

from teamscale_client import TeamscaleClient

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)

    client.upload_architectures({"architectures/system.architecture": "/path/to/system.architecture"},
                                "Upload architecture", timestamp=datetime.datetime.now())
