from teamscale_client.utils import auto_str


@auto_str
class MergeRequest(object):
    """Represents a Merge Request in Teamscale

    Args:
        id (int): The merge request id
        id_with_repo (str): The merge request id appended to the repository name
        status (long): The merge request status
        title (str): The merge request title
        source_branch (str): The merge request source branch
        source_head (str): The commit sha on head (source branch)
        target_branch (str): The branch to which the MR is intended to merge
        url (str): The full SCM url of the branch
        voting_record (VotingRecord): the voting data associated with the MR
        findings_churn_count (FindingsChurnCount): the findings churn stats
    """
    # TODO not getting all the identifier fields from the reponse. Let's add the rest if needed
    def __init__(self, id, id_with_repo, status, title, source_branch, source_head, target_branch, url, voting_record,
                 findings_churn_count):
        self.id = id
        self.id_with_repo = id_with_repo
        self.status = status
        self.title = title
        self.source_branch = source_branch
        self.source_head = source_head
        self.target_branch = target_branch
        self.url = url
        self.voting_record = voting_record
        self.findings_churn_count = findings_churn_count

    def print_mr(self):
        print(f"{self.id_with_repo} - {self.status} : {self.url}")

    def get_id_with_repo(self):
        return self.id_with_repo

    def get_source_branch(self):
        return self.source_branch

    @classmethod
    def from_json(cls, json):
        try:
            voting = VotingRecord.from_json(json['votingRecord'])
        except KeyError:
            voting = None

        try:
            findings_churn = FindingsChurnCount.from_json(json['findingChurnCount'])
        except KeyError:
            findings_churn = None

        return MergeRequest(json['mergeRequest']['identifier']['id'],
                            json['mergeRequest']['identifier']['idWithRepository'],
                            json['mergeRequest']['status'], json['mergeRequest']['title'],
                            json['mergeRequest']['sourceBranch'], json['mergeRequest']['sourceHead'],
                            json['mergeRequest']['targetBranch'], json['mergeRequest']['url'], voting, findings_churn)


@auto_str
class VotingRecord(object):
    """Represents a Teamscale Voting Record for a given MR in Teamscale

    Args:
        timestamp (double): When Teamscale created the voting record
        state (str): The voting state
        commit (Commit): The merge request title
        comment (str): The merge request source branch
        partitions_included_in_vote ([str]): The commit sha on head (source branch)
    """

    def __init__(self, timestamp, state, commit, comment, partitions_included_in_vote):
        self.timestamp = timestamp
        self.state = state
        self.commit = commit
        self.comment = comment
        self.partitions_included_in_vote = partitions_included_in_vote

    @classmethod
    def from_json(cls, json):
        return VotingRecord(json['timestamp'], json['state'], Commit.from_json(json['commit']), json['comment'],
                            json['partitionsIncludedInVote'])


@auto_str
class Commit(object):
    """Represents a Teamscale commit in the voting context

    Args:
        type (str): Type of voting commit
        branch_name (str): the branch name where voting happened
        timestamp (double): when Teamscale created the voting commit
    """
    # TODO: not getting here parentCommits field. Let's add it if necessary
    def __init__(self, type, branch_name, timestamp):
        self.type = type
        self.branch_name = branch_name
        self.timestamp = timestamp

    @classmethod
    def from_json(cls, json):
        return Commit(json['type'], json['branchName'], json['timestamp'])


@auto_str
class FindingsChurnCount(object):
    """Represents a findings churn count for the MR

    Args:
        added_findings (int): The number of added findings
        findings_added_in_branch (int): The number of findings added in branch (only on merges)
        findings_in_changed_code (int): The number of findings that are old and in changed code
        removed_findings (int): The number of removed findings
        findings_removed_in_branch (int): The number of findings removed in branch (only on merges)
    """

    def __init__(self, added_findings, findings_added_in_branch, findings_in_changed_code, removed_findings,
                 findings_removed_in_branch):
        self.added_findings = added_findings
        self.findings_added_in_branch = findings_added_in_branch
        self.findings_in_changed_code = findings_in_changed_code
        self.removed_findings = removed_findings
        self.findings_removed_in_branch = findings_removed_in_branch

    def get_added_findings(self):
        return self.added_findings

    def get_findings_added_in_branch(self):
        return self.findings_added_in_branch

    def get_findings_in_changed_code(self):
        return self.findings_in_changed_code

    def get_removed_findings(self):
        return self.removed_findings

    def get_findings_removed_in_branch(self):
        return self.findings_removed_in_branch
    @classmethod
    def from_json(cls, json):
        return FindingsChurnCount(json['addedFindings'], json['findingsAddedInBranch'], json['findingsInChangedCode'],
                                  json['removedFindings'], json['findingsRemovedInBranch'])
