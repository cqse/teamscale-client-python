from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import time
import os
import json
import argparse

from ConfigParser import ConfigParser

from teamscale_client.git_utils import get_current_branch, get_current_timestamp
from teamscale_client.git_utils import get_changed_files_and_content, get_deleted_files
from teamscale_client.data import PreCommitUploadData
from teamscale_client import TeamscaleClient
from teamscale_client.teamscale_config import TeamscaleConfig
from teamscale_client.git_utils import get_repo_root_from_file_in_repo


class PrecommitClient:
    """Client for precommit analysis"""
    def __init__(self, teamscale_config, repository_path, analyzed_file=None):
        """Constructor"""
        self.repository_path = repository_path
        self.teamscale_client = TeamscaleClient(teamscale_config.url, teamscale_config.username,
                                                teamscale_config.access_token, teamscale_config.project_id)
        self.analyzed_file = analyzed_file


    def upload_precommit_data(self):
        """Uploads the currently changed files for precommit analysis."""
        current_branch = get_current_branch(self.repository_path)
        self.teamscale_client.branch = current_branch
        print('Current branch: %s' % current_branch)

        parent_commit_timestamp = get_current_timestamp(self.repository_path)
        print('Parent commit timestamp: %s' % parent_commit_timestamp)

        changed_files = get_changed_files_and_content(self.repository_path)
        deleted_files = get_deleted_files(self.repository_path)

        precommit_data = PreCommitUploadData(uniformPathToContentMap=changed_files, deletedUniformPaths=deleted_files)
        self.teamscale_client.upload_files_for_precommit_analysis(
            datetime.datetime.fromtimestamp(int(parent_commit_timestamp)), precommit_data)


    def get_precommit_results(self):
        """Gets the current precommit results. Waits synchronously until server is ready. """
        return self.teamscale_client.get_precommit_analysis_results()


    def print_precommit_results_as_error_string(self, include_findings_in_changed_code=True,
                                                include_existing_findings=False, include_all_findings=False):
        """Print the current precommit results formatting them in a way, most text editors understand."""
        added_findings, removed_findings, findings_in_changed_code = self.get_precommit_results()

        print('New findings:')
        for formatted_finding in self._format_findings(added_findings):
            print(formatted_finding)

        if include_findings_in_changed_code:
            print('')
            print('Findings in changed code:')
            for formatted_finding in self._format_findings(findings_in_changed_code):
                print(formatted_finding)

        uniform_path = os.path.relpath(self.analyzed_file, self.repository_path)
        if include_all_findings:
            uniform_path = ''

        if include_existing_findings or include_all_findings:
            existing_findings = self.teamscale_client.get_findings(
                uniform_path=uniform_path,
                timestamp=datetime.datetime.fromtimestamp(int(get_current_timestamp(self.repository_path))))
            print('')
            print('Existing findings:')
            for formatted_finding in self._format_findings(existing_findings):
                print(formatted_finding)


    def _format_findings(self, findings):
        """Formats the given findings as error or warning strings."""
        if len(findings) == 0:
            return ['> No findings.']
        sorted_findings = sorted(findings)
        return [os.path.join(self.repository_path, finding.uniformPath) + ':' + unicode(finding.startLine) + ':0: ' +
                self._severity_string(finding=finding) + ': ' + finding.message for finding in sorted_findings]


    def _severity_string(self, finding):
        """Formats the given finding's assessment as severity."""
        if finding.assessment == 'RED':
            return 'error'
        else:
            return 'warning'


precommit_config_filename = '.teamscale-precommit.config'


def _parse_args():
    """Parses the precommit client command line arguments."""
    parser = argparse.ArgumentParser(description='Precommit analysis client for Teamscale.')
    parser.add_argument('path', metavar='path', type=str, nargs=1,
                        help='path to any file in the repository')
    parser.add_argument('--exclude-findings-in-changed-code', dest='exclude_findings_in_changed_code',
                        action='store_const', const=True, default=False,
                        help='Determines whether to exclude findings in changed code (default: False)')
    parser.add_argument('--fetch-existing-findings', dest='fetch_existing_findings', action='store_const',
                        const=True, default=False,
                        help='When this option is set, existing findings in the specified file are fetched in addition '
                             'to precommit findings. (default: False)')
    parser.add_argument('--fetch-all-findings', dest='fetch_all_findings', action='store_const',
                        const=True, default=False,
                        help='When this option is set, all existing findings in the repo are fetched in addition '
                             'to precommit findings. (default: False)')
    return parser.parse_args()


def configure_precommit_client(config_file, repo_path, parsed_args):
    """Reads the precommit analysis configuration and creates a precommit client with the corresponding config."""
    parser = ConfigParser()
    parser.read(config_file)
    config = TeamscaleConfig(url=parser.get('teamscale', 'url'), username=parser.get('teamscale', 'username'),
                             access_token=parser.get('teamscale', 'access_token'),
                             project_id=parser.get('project', 'id'))
    return PrecommitClient(teamscale_config=config, repository_path=repo_path, analyzed_file=parsed_args.path[0])


def analyze():
    """Performs precommit analysis."""
    parsed_args = _parse_args()
    repo_path = get_repo_root_from_file_in_repo(parsed_args.path[0])
    if not repo_path or not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        raise RuntimeError('Invalid path to file in repository: %s' % repo_path)

    print('Configuring precommit analysis...')

    config_file = os.path.join(repo_path, precommit_config_filename)
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        raise RuntimeError('Config file could not be found: %s' % config_file)
    precommit_client = configure_precommit_client(config_file=config_file, repo_path=repo_path, parsed_args=parsed_args)

    print('Uploading changes for precommit analysis for repo at %s...' % repo_path)
    precommit_client.upload_precommit_data()

    # We need to wait for the analysis to pick up the new code otherwise we get old findings
    time.sleep(2)

    print('Querying precommit analysis results...')
    print('')
    precommit_client.print_precommit_results_as_error_string(
        include_findings_in_changed_code=not parsed_args.exclude_findings_in_changed_code,
        include_existing_findings=parsed_args.fetch_existing_findings,
        include_all_findings=parsed_args.fetch_all_findings)


if __name__ == '__main__':
    analyze()
