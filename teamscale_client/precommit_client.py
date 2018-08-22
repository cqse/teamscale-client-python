from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import time
import os
import sys
import json

from teamscale_client.git_utils import get_current_branch, get_current_timestamp
from teamscale_client.git_utils import get_changed_files_and_content, get_deleted_files
from teamscale_client.data import PreCommitUploadData
from teamscale_client import TeamscaleClient
from teamscale_client.teamscale_config import TeamscaleConfig
from teamscale_client.git_utils import get_repo_root_from_file_in_repo


class PrecommitClient:
    """Client for precommit analysis"""
    def __init__(self, teamscale_config, repository_path):
        """Constructor"""
        self.repository_path = repository_path
        self.teamscale_client = TeamscaleClient(teamscale_config.url, teamscale_config.username,
                                                teamscale_config.access_token, teamscale_config.project_id)


    def upload_precommit_data(self):
        """Uploads all currently changed files to Teamscale for precommit analysis."""
        current_branch = get_current_branch(self.repository_path)
        self.teamscale_client.branch = current_branch
        print('Current branch: %s' % current_branch)

        parent_commit_timestamp = get_current_timestamp(self.repository_path)
        print('Parent commit timestamp: %s' % parent_commit_timestamp)

        changed_files = get_changed_files_and_content(self.repository_path)
        deleted_files = get_deleted_files(self.repository_path)

        precommit_data = PreCommitUploadData(uniformPathToContentMap=changed_files, deletedUniformPaths=deleted_files)
        self.teamscale_client.upload_files_for_precommit_analysis(
            datetime.datetime.fromtimestamp(parent_commit_timestamp), precommit_data)


    def get_precommit_results(self):
        """Gets the current precommit results. Waits synchronously until server is ready. """
        return self.teamscale_client.get_precommit_analysis_results()


    def print_precommit_results_as_error_string(self, include_findings_in_changed_code=True):
        """Print the current precommit results formatting them in a way, most text editors understand."""

        added_findings, removed_findings, findings_in_changed_code = self.get_precommit_results()

        print("New findings:")
        for formatted_finding in self._format_findings(added_findings):
            print(formatted_finding)

        if include_findings_in_changed_code:
            print("")
            print("Findings in changed code:")
            for formatted_finding in self._format_findings(findings_in_changed_code):
                print(formatted_finding)


    def _format_findings(self, findings):
        """Formats the given findings as error strings."""
        # return [os.path.split(finding.uniformPath)[1] + ':' + unicode(finding.startLine) + ':0: error: '
        #         + finding.message for finding in findings]
        return [os.path.join(repo_path, finding.uniformPath) + ':' + unicode(finding.startLine) + ':0: error: '
                + finding.message for finding in findings]


precommit_config_filename = ".teamscale-precommit.config"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError("Expected path to any file in the repository as parameter")

    any_path_in_repo = sys.argv[1]
    repo_path = get_repo_root_from_file_in_repo(any_path_in_repo)
    if not repo_path or not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        raise RuntimeError("Invalid path to file in repository: %s" % repo_path)

    print("Reading precommit analysis config...")

    config_file = os.path.join(repo_path, precommit_config_filename)
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        raise RuntimeError("Config file could not be found: %s" % config_file)

    with open(config_file) as config_data_file:
        configuration = json.load(config_data_file)

    config_ts = configuration['teamscale']
    config_project = configuration['project']
    config = TeamscaleConfig(url=config_ts['url'], username=config_ts['username'],
                             access_token=config_ts['access_token'], project_id=config_project['project_id'])

    precommit_client = PrecommitClient(teamscale_config=config, repository_path=repo_path)

    print("Uploading changes for precommit analysis for repo at %s..." % repo_path)
    precommit_client.upload_precommit_data()

    time.sleep(2)

    print("Querying precommit analysis results...")
    print("")
    precommit_client.print_precommit_results_as_error_string(
        include_findings_in_changed_code=config_project['query_findings_in_changed_code'])
