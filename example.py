from __future__ import print_function

import datetime

from teamscale_client import TeamscaleClient

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
PASSWORD = "admin"

PROJECT_NAME = "foo"

if __name__ == '__main__':
    findings = [
        {
            "findings": [
                {
                    "findingTypeId": "externals-2-type-2",
                    "message": "test",
                    "assessment": "RED",
                    "startLine": 1,
                    "endLine": 1,
                    "startOffset": 1,
                    "endOffset": 26
                }
            ],
            "path": "src/main/java/junit/extensions/ActiveTestSuite.java"
        }
    ]
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)
    response = client.upload_findings(findings, datetime.datetime.now(), "TestCommit", "test-partition")
    print("Request result: %s" % (response.text,))
