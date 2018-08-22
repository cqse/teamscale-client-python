from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from teamscale_client.teamscale_config import TeamscaleConfig
from teamscale_client.precommit_client import PrecommitClient

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "Okr1yMvcDC5Y0WySzIWzgHvTZEq3QGOl"
PROJECT_ID = "teamscale-python-client"
REPO_PATH = '/Users/pagano/GIT/teamscale-client-python'


if __name__ == '__main__':
    config = TeamscaleConfig(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)
    precommit_client = PrecommitClient(repository_path=REPO_PATH, teamscale_config=config)
    precommit_client.upload_precommit_data()
    # added_findings, removed_findings, findings_in_changed_code = precommit_client.get_precommit_results()
    #
    # print('Added findings: %s' % added_findings)
    # print('Removed findings: %s' % removed_findings)
    # print('Findings in changed code: %s' % findings_in_changed_code)
    # filename:rawStartLine:0: error: message

    precommit_client.get_precommit_results_as_error_string()

