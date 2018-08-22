from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.data import PreCommitUploadData
from teamscale_client.git_utils import get_current_branch, get_current_timestamp, get_changed_files

TEAMSCALE_URL = "http://localhost:8081"

USERNAME = "admin"
ACCESS_TOKEN = "YdzI_HgK6fHQNqOiwQG8FWD0cM9zwwB0"
PROJECT_ID = "teamscale-python-client"


def show_findings(client):
    baselines = client.get_baselines()
    print([str(baseline) for baseline in baselines])


if __name__ == '__main__':

    branch = get_current_branch('/Users/pagano/GIT/teamscale-client-python')
    timestamp = get_current_timestamp('/Users/pagano/GIT/teamscale-client-python')
    get_changed_files('/Users/pagano/GIT/teamscale-client-python')

    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID, branch=branch)

    precommit_data = PreCommitUploadData(uniformPathToContentMap={'x.java': 'import java.lang.String;'},
                                         deletedUniformPaths=[])
    client.upload_files_for_precommit_analysis(datetime.datetime.fromtimestamp(timestamp), precommit_data)

