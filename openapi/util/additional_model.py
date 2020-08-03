from util.general_utils import auto_str
from util.constants import ConnectorType
from openapi_client.models import ConnectorConfiguration


@auto_str
class SourceCodeConnectorConfiguration(ConnectorConfiguration):
    """Represents a Teamscale source code connector configuration.

    Args:
        connector_type (constants.ConnectorType): The connector type of this configuration.
        included_file_names (str): Ant patterns describing the files to be read from the repository.
        excluded_file_names (Optional[str]): Ant patterns describing the files to be excluded from the repository.
        repository_identifier (Optional[str]): A unique identifier used to reference the repository. This is also shown
                                               in the UI and should have a meaningful value. Defaults to 'repository1'.
        enable_branch_analysis (Optional[bool]): Whether not only the main line but also branches should be analyzed.
                                                 Defaults to `False`.
        included_branches (Optional[str]): Regex patterns describing the branches to be read from the repository.
                                           All branches are included by default.
        excluded_branches (Optional[str]): Regex patterns describing the branches to be excluded from the repository.
                                           Defaults to `_anon.*`.
        start_revision (Optional[str]): The first date or revision to be read. If left empty, the entire history
                                        will be read.
        content_exclude (Optional[str]): A comma-separated list of filters that removes the complete content of a file
                                         (i.e. treating it as an empty file) based on a regular expression matched
                                         against the file's content.
        polling_interval (Optional[int]): Delay used for polling the repository in seconds (default is 60 seconds).
        prepend_repository_identifier (Optional[bool]): Whether to include the repository identifier as a prefix
                                                        for the created file paths. Defaults to `False`.
        end_revision (Optional[str]): The last date or revision to be read. If left empty, the history up to
                                      the latest revision is read.
        text_filter (Optional[str]): A comma-separated list of regular expressions describing what parts of a file
                                     should be excluded from analysis, e.g. generated code.
        source_library_connector (Optional[bool]): If this is true, the contained files will only be used
                                                   for source library lookup, but not for analysis. Defaults to `False`.
        run_to_exhaustion (Optional[bool]): If this is true, the repository will not be polled after
                                            the current head is reached. Defaults to `False`.
        delta_size (Optional[int]): Adjusts the size of deltas produced by the connector (experts only, default is 500).
        path_prefix_transformation (Optional[str]): Prefix transformations that are applied to the paths
                                                    from the repository. Empty by default.
        path_transformation (Optional[str]): Regex transformations that are applied to the paths
                                             from the repository. Empty by default.
        encoding (Optional[str]): This can be used to set the encoding used (e.g. UTF-8, latin1) when reading files.
                                  Empty by default.
        author_transformation (Optional[str]): Regex transformations that are applied to the authors of the repository.
                                               Empty by default.
        branch_transformation (Optional[str]): Regex transformations that are applied to the branch names
                                               of the repository. Empty by default.
    """

    def __init__(self, connector_type, included_file_names, excluded_file_names="", repository_identifier="repository1",
                 enable_branch_analysis=False, included_branches=".*", excluded_branches="_anon.*", start_revision="",
                 content_exclude="", polling_interval=60, prepend_repository_identifier=False, end_revision="",
                 text_filter="", source_library_connector=False, run_to_exhaustion=False, delta_size=500,
                 path_prefix_transformation="", path_transformation="", encoding="", author_transformation="",
                 branch_transformation="", preserve_empty_commits=False):
        super(SourceCodeConnectorConfiguration, self).__init__(connector_type)
        self.options = {
            "Included file names": included_file_names,
            "Excluded file names": excluded_file_names,
            "Repository identifier": repository_identifier,
            "Enable branch analysis": enable_branch_analysis,
            "Included branches": included_branches,
            "Excluded branches": excluded_branches,
            "Start revision": start_revision,
            "Content exclude": content_exclude,
            "Polling interval": polling_interval,
            "Prepend repository identifier": prepend_repository_identifier,
            "End revision": end_revision,
            "Text filter": text_filter,
            "Source library connector": source_library_connector,
            "Run to exhaustion": run_to_exhaustion,
            "Delta size": delta_size,
            "Path prefix transformation": path_prefix_transformation,
            "Path transformation": path_transformation,
            "Encoding": encoding,
            "Author transformation": author_transformation,
            "Branch transformation": branch_transformation,
            "Preserve empty commits": preserve_empty_commits
        }


@auto_str
class FileSystemSourceCodeConnectorConfiguration(SourceCodeConnectorConfiguration):
    """Represents a Teamscale file system connector configuration.

    Args:
        input_directory (str): Path to the directory that should be analyzed
    """

    def __init__(self, input_directory, *args, **kwargs):
        super(FileSystemSourceCodeConnectorConfiguration, self).__init__(connector_type=ConnectorType.FILE_SYSTEM,
                                                                         *args, **kwargs)
        self.options["Input directory"] = input_directory


@auto_str
class MultiVersionFileSystemSourceCodeConnectorConfiguration(SourceCodeConnectorConfiguration):
    """Represents a Teamscale multiversion file system connector configuration.

    Args:
        input_directory (str): Path to the directory that should be analyzed
    """

    def __init__(self, input_directory, *args, **kwargs):
        super(MultiVersionFileSystemSourceCodeConnectorConfiguration, self).__init__(
            connector_type=ConnectorType.MULTI_VERSION_FILE_SYSTEM, *args, **kwargs)
        self.options["Input directory"] = input_directory


@auto_str
class GitSourceCodeConnectorConfiguration(SourceCodeConnectorConfiguration):
    """Represents a Teamscale Git connector configuration.

    Args:
        default_branch_name (str): Name of the branch that should be analyzed. If not provided, the master branch will be used.
                           If `enable_branch_analysis` is set to `True`, this becomes the default branch.
        account (str): Name of the Teamscale account to use to connect to the repository.
        path_suffix (Optional[str]): The suffix to append to the base URL of the repository. Empty by default.
        include_submodules (Optional[bool]): Whether to transparently analyze submodules. Defaults to `False`.
        submodule_recursion_depth (Optional[int]): The maximum recursion depth when analyzing submodules.
                                                   Defaults to `10`.
    """

    def __init__(self, default_branch_name, account, path_suffix="", include_submodules=False,
                 submodule_recursion_depth=10, connector_type=ConnectorType.GIT, *args, **kwargs):
        super(GitSourceCodeConnectorConfiguration, self).__init__(connector_type=connector_type, *args, **kwargs)
        self.options["Default branch name"] = default_branch_name
        self.options["Account"] = account
        self.options["Path suffix"] = path_suffix
        self.options["Include Submodules"] = include_submodules
        self.options["Submodule recursion depth"] = submodule_recursion_depth


@auto_str
class GerritSourceCodeConnectorConfiguration(GitSourceCodeConnectorConfiguration):
    """Represents a Teamscale Gerrit connector configuration.

    Args:
        project_name (str): Used to reference the project.
        enable_voting (str): Enables Teamscale voting on Gerrit reviews.
        enable_detailed_line_comments (str): When enabled, a Teamscale vote will carry a detailed comment for each
                                             generated finding that is annotated to the relevant line in the reviewed
                                             file.
        ignore_yellow_findings_for_votes (str): When enabled, Teamscale will only consider red findings when voting.
        ignore_yellow_findings_for_comments (str): When enabled, Teamscale will only consider red findings when
                                                   commenting.
        number_of_ref_batches_for_updates (str): Defines the number of seperate parts the refs are fetched from Gerrit.
                                                 Can be between 1-100, but 100 must be cleanly dividable by the given
                                                 number. DO NOT CHANGE THIS, unless you know exactly what you are doing.
        review_label (str): The review label used to upload feedback to Gerrit.
    """

    def __init__(self, project_name, enable_voting=False, enable_detailed_line_comments=True,
                 ignore_yellow_findings_for_votes=False, ignore_yellow_findings_for_comments=False,
                 number_of_ref_batches_for_updates=1, review_label="Code-Review", *args, **kwargs):
        super(GerritSourceCodeConnectorConfiguration, self).__init__(connector_type=ConnectorType.GERRIT, *args,
                                                                     **kwargs)
        self.options["Project Name"] = project_name
        self.options["Enable Voting"] = enable_voting
        self.options["Enable Detailed Line Comments"] = enable_detailed_line_comments
        self.options["Ignore Yellow Findings For Votes"] = ignore_yellow_findings_for_votes
        self.options["Ignore Yellow Findings For Comments"] = ignore_yellow_findings_for_comments
        # self.options["Number of Ref Batches For Updates"] = number_of_ref_batches_for_updates
        self.options["Review Label"] = review_label


@auto_str
class TFSSourceCodeConnectorConfiguration(SourceCodeConnectorConfiguration):
    """Represents a Teamscale TFS connector configuration.

    Args:
        account (str): Name of the Teamscale account to use to connect to the repository.
        branch_path_suffix (Optional[str]): The suffix to append to the branch name. Empty by default.
        path_suffix (Optional[str]): The suffix to append to the base URL of the repository. Empty by default.
        branch_lookup_paths (Optional[str]): Sub paths in which to look for branches. Empty by default.
    """

    def __init__(self, account, branch_path_suffix="", path_suffix="", branch_lookup_paths="", *args, **kwargs):
        super(TFSSourceCodeConnectorConfiguration, self).__init__(connector_type=ConnectorType.TFS, *args, **kwargs)
        self.options["Account"] = account
        self.options["Branch path suffix"] = branch_path_suffix
        self.options["Path suffix"] = path_suffix
        self.options["Branch lookup paths"] = branch_lookup_paths


@auto_str
class SubversionSourceCodeConnectorConfiguration(SourceCodeConnectorConfiguration):
    """Represents a Teamscale Subversion connector configuration.

    Args:
        account (str): Name of the Teamscale account to use to connect to the repository.
        enable_externals (Optional[bool]): Whether to also parse and interpret svn:externals properties.
                                           Defaults to `False`.
        externals_includes (Optional[str]): Ant patterns describing the directories that are checked for svn:externals.
                                            Empty by default.
        externals_excludes (Optional[str]): Ant patterns describing the directories that are not checked for
                                            svn:externals. Empty by default.
        path_suffix (Optional[str]): Path suffix that is to be appended to the repository's base path. Empty by default.
    """

    def __init__(self, account, enable_externals=False, externals_includes="", externals_excludes="", path_suffix="", *args, **kwargs):
        super(SubversionSourceCodeConnectorConfiguration, self).__init__(connector_type=ConnectorType.SVN, *args,
                                                                         **kwargs)
        self.options["Account"] = account
        self.options["Enable Externals"] = enable_externals
        self.options["Path suffix"] = path_suffix
        self.options["Externals Includes"] = externals_includes
        self.options["Externals Excludes"] = externals_excludes


