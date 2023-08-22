from datetime import datetime

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

    def print_teamscale_mr_url(self, teamscale_base_url, project):
        print(f"{self.id_with_repo} - {self.status} : {teamscale_base_url}{project}/{self.id_with_repo}")

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

    def print_churn(self):
        print("  => Findings Churn Count:")
        print(f"    Added:  {self.get_added_findings()}")
        print(f"    Added in branch: {self.get_findings_added_in_branch()}")
        print(f"    In changed code: {self.get_findings_in_changed_code()}")
        print(f"    Removed: {self.get_removed_findings()}")
        print(f"    Removed in branch: {self.get_findings_removed_in_branch()}")

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        return FindingsChurnCount(json['addedFindings'], json['findingsAddedInBranch'], json['findingsInChangedCode'],
                                  json['removedFindings'], json['findingsRemovedInBranch'])


@auto_str
class CommitFindings(object):
    """Represents findings data related to a commit

    Args:
        removed_findings_count (int):
        added_findings_count (int):
        removed_findings (List[Finding]):
        added_findings(List[Finding]):
    """

    def __init__(self, removed_findings_count, added_findings_count, removed_findings, added_findings):
        self.removed_findings_count = removed_findings_count
        self.added_findings_count = added_findings_count
        self.removed_findings = removed_findings
        self.added_findings = added_findings

    def get_removed_findings_count(self):
        return self.removed_findings_count

    def get_removed_findings(self):
        return self.removed_findings

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        return CommitFindings(json['removedFindingsCount'], json['addedFindingsCount'],
                              [Finding.from_json(removed_f) for removed_f in json['removedFindings']],
                              [Finding.from_json(added_f) for added_f in json['addedFindings']])


@auto_str
class Finding(object):
    """Represents a Teamscale finding

    Args:
        f_id (str): Finding unique id in Teamscale
        group_name (str): Finding group in Teamscale
        category_name (str): Finding categoru in Teamscale
        message (str): Finding message in Teamscale
        assessment (constants.Assessment): The assessment this finding should have. Default is `YELLOW`.
                                            This value is only important if in Teamscale the finding enablement
                                            is set to auto, otherwise the setting from Teamscale will be used.
        location (FindingLocation): location data for the finding
        birth(FindingBirth):
        death(FindingDeath):
    """

    def __init__(self, f_id, group_name, category_name, message, assessment, location, birth, death):
        self.f_id = f_id
        self.group_name = group_name
        self.category_name = category_name
        self.message = message
        self.assessment = assessment
        self.location = location
        self.birth = birth
        self.death = death

    def get_birth(self):
        return self.birth

    def get_id(self):
        return self.f_id

    def print(self):
        print("           Finding id: " + self.f_id)
        print("           Finding uniformPath: " + self.location.get_uniform_path())
        print("           Finding message: " + self.message)
        print("           Introduction date/time: " + str(datetime.fromtimestamp(self.birth.get_timestamp() / 1000)))
        if self.death:
            print("           Removal date/time: " + str(datetime.fromtimestamp(self.death.get_timestamp() / 1000)))

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        try:
            death = FindingDeath.from_json(json['death'])
        except KeyError:
            death = None
        return Finding(json['id'], json['groupName'], json['categoryName'], json['message'], json['assessment'],
                       FindingLocation.from_json(json['location']), FindingBirth.from_json(json['birth']), death)


@auto_str
class FindingLocation(object):
    """Represents the location of a Teamscale finding

    Args:
        f_type (str): Finding type in Teamscale
        uniform_path (str): Uniform path of the finding group in Teamscale
        raw_start_offset (int): Start offset of the finding
        raw_end_offset (int): End offset of the finding
        raw_start_line (int): Line where the finding starts
        raw_end_line(int): Line where the finding ends
        location(str): file path where the finding is located
    """

    def __init__(self, f_type, uniform_path, raw_start_offset, raw_end_offset, raw_start_line, raw_end_line, location):
        self.f_type = f_type
        self.uniform_path = uniform_path
        self.raw_start_offset = raw_start_offset
        self.raw_end_offset = raw_end_offset
        self.raw_start_line = raw_start_line
        self.raw_end_line = raw_end_line
        self.location = location

    def get_uniform_path(self):
        return self.uniform_path

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        return FindingLocation(json['type'], json['uniformPath'], json['rawStartOffset'], json['rawEndOffset'],
                               json['rawStartLine'], json['rawEndLine'], json['location'])


@auto_str
class FindingBirth(object):
    """Represents data about the finding introduction

    Args:
        f_type (str): Type of finding introduction
        branch_name (str): Branch where the finding was introduced
        timestamp (double): When the finding was introduced
    """

    def __init__(self, f_type, branch_name, timestamp):
        self.f_type = f_type
        self.branch_name = branch_name
        self.timestamp = timestamp

    def get_timestamp(self):
        return self.timestamp

    def get_branch_name(self):
        return self.branch_name

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        return FindingBirth(json['type'], json['branchName'], json['timestamp'])


@auto_str
class FindingDeath(object):
    """Represents data about the finding removal

    Args:
        f_type (str): Type of finding removal
        branch_name (str): Branch where the finding was removed
        timestamp (double): When the finding was removed
    """

    def __init__(self, f_type, branch_name, timestamp):
        self.f_type = f_type
        self.branch_name = branch_name
        self.timestamp = timestamp

    def get_timestamp(self):
        return self.timestamp

    @classmethod
    def from_json(cls, json):
        if json is None:
            return
        return FindingDeath(json['type'], json['branchName'], json['timestamp'])
