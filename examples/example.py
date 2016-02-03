from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import sys

from teamscale_client import TeamscaleClient
from teamscale_client.constants import Enablement
from teamscale_client.data import Finding, FileFindings, FindingDescription


TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
PASSWORD = "admin"

PROJECT_NAME = "test"

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)

    # Add a new group that will contain findings
    response = client.add_findings_group("Group 1", "externals-.*")
    print("Request result: %s" % (response.text,))

    # Make Teamscale aware of a new findings type, which mappes to the previously
    # created group
    descriptions = [
        FindingDescription("externals-1", "A test finding description", Enablement.RED)
    ]
    response = client.add_finding_descriptions(descriptions)
    print("Request result: %s" % (response.text,))

    # A manual step to add the new groups to existing analysis profiles has to be done.
    if sys.version_info[0] == 2:
        raw_input("Please create the project or update the analysis profile used by the project to contain the new groups. Then Press ENTER to continue.")
    else:
        input("Please create the projetc or update the analysis profile used by the project to contain the new groups. Then Press ENTER to continue.")

    # Update existing project to use new findings
    response = client.update_findings_schema()
    print("Request result: %s" % (response.text,))

    # Upload findings to Teamscale
    findings = [
        FileFindings([
                      Finding("externals-1", "test2", start_line=3)
                      ],
                      "src/Foo.java")
    ]
    response = client.upload_findings(findings, datetime.datetime.now(), "TestCommit", "test-partition")
    print("Request result: %s" % (response.text,))
