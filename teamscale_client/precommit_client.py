import datetime

from teamscale_client.git_utils import get_current_branch, get_current_timestamp, get_changed_files_and_content, get_deleted_files
from teamscale_client.data import PreCommitUploadData


class PrecommitClient:
    """Client for precommit analysis"""
    def __init__(self, repository_path, teamscale_client):
        """Constructor
        """
        self.repository_path = repository_path
        self.teamscale_client = teamscale_client

    def upload_precommit_data(self):
        current_branch = get_current_branch(self.repository_path)
        self.teamscale_client.branch = current_branch

        parent_commit_timestamp = get_current_timestamp(self.repository_path)
        changed_files = get_changed_files_and_content(self.repository_path)
        deleted_files = get_deleted_files(self.repository_path)

        precommit_data = PreCommitUploadData(uniformPathToContentMap=changed_files, deletedUniformPaths=deleted_files)
        self.teamscale_client.upload_files_for_precommit_analysis(
            datetime.datetime.fromtimestamp(parent_commit_timestamp), precommit_data)
