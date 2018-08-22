import os
from pygit2 import Repository, GIT_STATUS_WT_DELETED, GIT_STATUS_WT_MODIFIED, GIT_STATUS_WT_RENAMED, GIT_STATUS_WT_TYPECHANGE, GIT_STATUS_INDEX_NEW, GIT_STATUS_INDEX_MODIFIED, GIT_STATUS_INDEX_DELETED

def get_current_branch(path_to_repository):
    """Utility method for getting the current branch from Git.

        Args:
            obj (object): The object that should be encoded.

        Returns:
            str: The current branch in the provided repo.
    """
    repo = Repository(path_to_repository)
    head = repo.lookup_reference("HEAD").resolve()
    return head.shorthand

def get_current_timestamp(path_to_repository):
    """Utility method for getting the current timestamp from Git.

        Args:
            obj (object): The object that should be encoded.

        Returns:
            str: The current branch in the provided repo.
    """
    repo = Repository(path_to_repository)
    head = repo.revparse_single('HEAD')
    return head.commit_time

def get_changed_files_and_content(path_to_repository):
    changed_files = get_changed_files(path_to_repository)
    return {filename: open(os.path.join(path_to_repository, filename), 'rb').read() for filename in changed_files}

def get_changed_files(path_to_repository):
    repo = Repository(path_to_repository)
    status_entries = repo.status()

    stati_considered_for_precommit = GIT_STATUS_INDEX_NEW | \
                                     GIT_STATUS_INDEX_MODIFIED | \
                                     GIT_STATUS_WT_MODIFIED | \
                                     GIT_STATUS_WT_RENAMED | \
                                     GIT_STATUS_WT_TYPECHANGE
    return [path for path, st in status_entries.iteritems() if st & stati_considered_for_precommit]

def get_deleted_files(path_to_repository):
    repo = Repository(path_to_repository)
    status_entries = repo.status()

    stati_deleted = GIT_STATUS_INDEX_DELETED | \
                    GIT_STATUS_WT_DELETED
    return [path for path, st in status_entries.iteritems() if st & stati_deleted]
