from __future__ import absolute_import
from __future__ import unicode_literals

import datetime
import time

from teamscale_client.constants import Assessment, MetricAggregation, MetricValueType, MetricProperties, \
    ConnectorType
from teamscale_client.utils import auto_str


@auto_str
class Finding(object):
    """Representation of a finding in Teamscale.
    
    Args:
        finding_type_id (str): The type id that this finding belongs to.
        message (str): The main finding message
        assesssment (constants.Assessment): The assessment this finding should have. Default is `YELLOW`.
                                            This value is only important if in Teamscale the finding enablement
                                            is set to auto, otherwise the setting from Teamscale will be used.
        start_offset (int): Offset from the beginning of the file, where the finding area starts
                            (zero-based, inclusive). Can be left blank, if the start/endline are given. It has to point to the beginning of a token (e.g., a keyword).
                            (See also: :ref:`FAQ - Offsets <faq-offsets>`).
        end_offset (int): Offset from the beginning of the file, where the finding area ends (zero-based, inclusive).
                          Can be left blank, if the start/endline are given. It has to point to the end of a token (e.g., a keyword). (See also:
                          :ref:`FAQ - Offsets <faq-offsets>`).
        start_line (int): The finding's first line (one-based, inclusive). Can be left blank, if the offsets are given.
        end_line (int): The finding's last line (one-based, inclusive). Can be left blank, if the offsets or start_line
                        are given.
        identifier (Optional[str]): Advanced usage! Path to special elements in Teamscale, e.g. Simulink model parts.
                                    If this is given, offsets and lines do not need to be filled.
        uniform_path (Optional[str]): The path of the file where the finding is located.
        properties (Optional[dict]): A map of String->Object properties associated with this finding.
        finding_id (str): The Teamscale internal id of this finding. Can be left empty for findings that do not yet have
                          an id.
    """

    def __init__(self, finding_type_id, message, assessment=Assessment.YELLOW, start_offset=None,
                 end_offset=None, start_line=None, end_line=None, identifier=None, uniform_path=None,
                 finding_properties=None, finding_id=None):
        self.findingTypeId = finding_type_id
        self.message = message
        self.assessment = assessment
        self.startOffset = start_offset
        self.endOffset = end_offset
        self.startLine = start_line
        self.endLine = end_line
        self.identifier = identifier

        self.uniformPath = uniform_path
        self.findingProperties = finding_properties
        self.finding_id = finding_id

    def __cmp__(self, other):
        """Compares this finding to another finding."""
        if self.uniformPath == other.uniformPath:
            return self.startLine.__cmp__(other.startLine)
        else:
            if self.uniformPath < other.uniformPath:
                return -1
            else:
                return 1

    def __eq__(self, other):
        """Checks if this finding is equal to the given finding."""
        if self.finding_id and other.finding_id:
            return self.finding_id == other.finding_id
        return ((self.uniformPath, self.startLine, self.assessment, self.message, self.endLine, self.endOffset,
                 self.findingTypeId, self.identifier, self.startOffset) ==
                (other.uniformPath, other.startLine, other.assessment, other.message, other.endLine, other.endOffset,
                 other.findingTypeId, other.identifier, other.startOffset))

    def __ne__(self, other):
        """Checks if this finding is not equal to the given finding."""
        return not (self == other)

    def __lt__(self, other):
        """Checks if this finding is less than the given finding."""
        return (self.uniformPath, self.startLine, self.endLine) < (other.uniformPath, other.startLine, other.endLine)

    def __gt__(self, other):
        """Checks if this finding is greater than the given finding."""
        return (self.uniformPath, self.startLine, self.endLine) > (other.uniformPath, other.startLine, other.endLine)

    def __le__(self, other):
        """Checks if this finding is less than or equal the given finding."""
        return (self == other) or ((self.uniformPath, self.startLine, self.endLine) <
                                   (other.uniformPath, other.startLine, other.endLine))

    def __ge__(self, other):
        """Checks if this finding is greater than or equal the given finding."""
        return (self == other) or ((self.uniformPath, self.startLine, self.endLine) >
                                   (other.uniformPath, other.startLine, other.endLine))


@auto_str
class FileFindings(object):
    """Representation of a file and its findings.
    
    Args:
        findings (List[:class:`Finding`]): A list containing all findings that are present in this file. 
        path (str): The path to the file in Teamscale.
        content (Optional[str]): The content of the file (can be left empty).
    """

    def __init__(self, findings, path, content=None):
        self.findings = findings
        self.path = path
        self.content = content


@auto_str
class FindingDescription(object):
    """Description of a finding type to be added at configuration time.

        Args:
            typeid (str): The id used to reference the finding type.
            name (str): Some UI friendly name for this description.
            description (str): The text to display that explains what this finding type is about (and ideally how to fix it). This text will be the same for each concrete instance of the finding.
            enablement (constants.Enablement): Describes the default enablement setting for this finding type, used when it is added to the analysis profile.
    """

    def __init__(self, typeid, description, enablement, name=None):
        self.typeid = typeid
        self.description = description
        self.enablement = enablement
        self.name = name


@auto_str
class MetricDescription(object):
    """Description of a metric type to be addded at configuration time.
    
    Args:
        metric_id (str): The globally unique metric id.
        display_name (str): The metric's name that is displayed in the UI.
        description (str): A description explaining what this metric means.
        group_id (str): the name of an analysis group under which the metric is placed (used to group the metrics in the
                        analysis profile).
        aggregation (constants.MetricAggregation): How this metric is supposed to be aggregated up the directory
                                                   hierarchy. Defaults to ``SUM``.
        value_type (constants.MetricValueType): Determines the metric's type. Defaults to ``NUMERIC``.
        properties (set[constants.MetricProperties]): Determines the metric's properties. This has effects on how/if the
                                                      metric is displayed and assessed. Defaults to ``(SIZE_METRIC, )``.
        """

    def __init__(self, metric_id, display_name, description, group_id, aggregation=MetricAggregation.SUM,
                 value_type=MetricValueType.NUMERIC, properties=(MetricProperties.SIZE_METRIC,)):
        self.metricId = metric_id
        self.analysisGroup = group_id
        self.metricDefinition = {
            "name": display_name,
            "aggregation": aggregation,
            "description": description,
            "properties": properties,
            "valueType": value_type
        }


@auto_str
class MetricEntry(object):
    """A container for adding metric values to a file.
    
    Args:
        path (str): Path to a resource in Teamscale (usually a file). 
                    This can also point to architecture components using the following syntax:
                    ``-architectures-/<architecture-name>/path/to/component/``
        metrics (dict[str, object]): A dictionary mapping from metric_id to metric value. The value depends on
                                     the metric type: Numeric: ``double``, Timestamp: ``int - unix timestamp
                                     in milliseconds``, Assessment: ``[<GREENVALUE>,<YELLOWVALUE>,<REDVALUE>]``
    """

    def __init__(self, path, metrics):
        self.path = path
        self.metrics = metrics


@auto_str
class NonCodeMetricEntry(object):
    """A container for adding non-code metrics to a project.
    
    Args:
        path (str): Arbitrary path to which the non-code metrics shall be attached.
        content (str): The content displayed as content for the path.
        count (int): The count value.
        assessment (dict[:class:`constants.AssessmentMetricColors`, int]): The assessment distribution for this path.
        time (double): The time used to create this result (e.g. unit test run time, or build duration).
    """

    def __init__(self, path, content="", count=1, assessment={}, time=0.0):
        self.path = path
        self.content = content
        self.count = count
        self.assessment = assessment
        self.time = time


@auto_str
class Baseline(object):
    """Represents a Teamscale baseline. Either the date or the timestamp must be given

    Args:
        name (str): The baseline's name
        description (str): The baseline's description
        date (Optional[datetime.datetime]): The date for which the baseline is set
        date (Optional[long]): The timestamp (in ms) for which the baseline is set
    """

    def __init__(self, name, description, date=None, timestamp=None):
        if timestamp is None and date is None:
            raise Exception("Either date or timestamp must be given.")
        self.name = name
        self.description = description
        self.timestamp = timestamp
        if date is not None:
            self._set_date(date)

    def __hash__(self):
        return hash((self.name, self.description, self.timestamp))

    def __eq__(self, other):
        return isinstance(other, Baseline) and hash(other) == hash(self)

    def _get_date(self):
        return datetime.datetime.fromtimestamp(float(self._timestamp))

    def _set_date(self, date_object):
        import sys
        if sys.version_info > (3,):
            long_type = int
        else:
            long_type = long
        self.timestamp = long_type(time.mktime(date_object.timetuple()) * 1000)

    date = property(_get_date, _set_date)


class ServiceError(Exception):
    """Teamscale service returned an error."""
    pass


@auto_str
class ProjectInfo(object):
    """Represents information about a Teamscale project. When querying information about a project in Teamscale,
    the result is an instance of this class.

    Args:
        project_id (str): The project's id
        name (str): The project's name
        description (Optional[str]): The project's description
        creation_timestamp (Optional[long]): The project's creation timestamp (in ms)
        deleting (Optional[bool]): Whether the project is currently being deleted
        reanalyzing (Optional[bool]): Whether the project is currently being reanalyzed
    """

    def __init__(self, project_id, name, description=None, creation_timestamp=None, alias=None, deleting=False,
                 reanalyzing=False):
        self.id = project_id
        self.name = name
        self.description = description
        self.creationTimestamp = creation_timestamp
        self.alias = alias
        self.deleting = deleting
        self.reanalyzing = reanalyzing


@auto_str
class ProjectConfiguration(object):
    """Represents a Teamscale project configuration. This is used to create new and update existing projects in
    Teamscale.

    Args:
        name (str): The project's name
        project_id (str): The project's id
        profile (str): The name of the profile used to analyse the project
        connectors (List[:class:`ConnectorConfiguration`]): List of all connectors used in the project configuration
        alias (Optional[str]): The project's alias
    """

    def __init__(self, name, project_id, profile, connectors, alias=None):
        self.name = name
        self.id = project_id
        self.profile = profile
        self.connectors = connectors
        self.alias = alias


@auto_str
class ConnectorConfiguration(object):
    """Represents a Teamscale connector configuration. Connectors allow to attach external tools such as source code
    repositories.

    Args:
        connector_type (constants.ConnectorType): The connector type of this configuration
    """

    def __init__(self, connector_type):
        self.type = connector_type


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
        self.connectorIdentifierOptionName = "Repository identifier"
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


@auto_str
class Task(object):
    """Represents a task in Teamscale

    Args:
        id (int): The task's id
        subject (str): The task's subject
        author (str): The task author's name
        description (str): The task's description
        assignee (str): The assigned user's name
        status (constants.TaskStatus): The task's status
        resolution (Optional[constants.TaskResolution]): The task's resolution
        findings (Optional[List[str]]): The findings attached to this task
        comments (Optional[List[Comment]]): Comments attached to this task
        tags (List[str]): Tags that have been added to this task
    """

    # noinspection PyPep8Naming
    def __init__(self, id, subject, author, description, assignee, status, resolution, findings, comments, tags,
                 created, updated, updatedBy):
        self.id = id
        self.subject = subject
        self.author = author
        self.description = description
        self.assignee = assignee
        self.status = status
        self.resolution = resolution
        self.findings = findings
        self.comments = comments
        self.tags = tags
        self.created = created
        self.updated = updated
        self.updatedBy = updatedBy

    @classmethod
    def from_json(cls, json):
        comments = []
        if json['comments']:
            for comment_json in json['comments']:
                comments.append(Comment.from_json(comment_json))
        return Task(json['id'], json['subject'], json['author'], json.get('description', ""), json.get('assignee', ''),
                    json['status'], json['resolution'], json['findings'], comments, json['tags'],
                    json['created'], json['updated'], json['updatedBy'])


@auto_str
class Comment(object):
    """Represents a comment on a Task in Teamscale

    Args:
        author (str): The author of this comment
        date (long): Creation date in ms
        text (str): The comment's text
        changeComment (bool): Whether this is a system generated change comment
    """

    # noinspection PyPep8Naming
    def __init__(self, author, date, text, changeComment=False):
        self.author = author
        self.date = date
        self.text = text
        self.changeComment = changeComment

    @classmethod
    def from_json(cls, json):
        return Comment(json['author'], json['date'], json['text'], json['changeComment'])
