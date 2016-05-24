from __future__ import absolute_import
from __future__ import unicode_literals

import collections
import datetime
import time

from teamscale_client.constants import Assessment, MetricAggregation, MetricValueType, MetricProperties, AssessmentMetricColors
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
        start_offset (int): Offset from the beginning of the file, where the finding area starts (zero-based, inclusive). Can be left blank, if the start/endline are given. (See also: :ref:`FAQ - Offsets <faq-offsets>`).
        end_offset (int): Offset from the beginning of the file, where the finding area ends (zero-based, inclusive). Can be left blank, if the start/endline are given. (See also: :ref:`FAQ - Offsets <faq-offsets>`).
        start_line (int): The finding's first line (one-based, inclusive). Can be left blank, if the offsets are given. 
        end_line (int): The finding's last line (one-based, inclusive). Can be left blank, if the offsets or start_line are given.
        identifier (Optional[str]): Advanced usage! Path to special elements in Teamscale, e.g. Simulink model parts. If this is given, offsets and lines do not need to be filled.  
    """

    def __init__(self, finding_type_id, message, assessment=Assessment.YELLOW, start_offset=None, end_offset=None, start_line=None, end_line=None, identifier=None):
        self.findingTypeId = finding_type_id
        self.message = message
        self.assessment = assessment
        self.startOffset = start_offset
        self.endOffset = end_offset
        self.startLine = start_line
        self.endLine = end_line
        self.identifier = identifier

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


FindingDescription = collections.namedtuple('FindingDescription', ['typeid', 'description', 'enablement'])
"""Description of a finding type to be added at configuration time.

    Args:
        typeid (str): The id used to reference the finding type.
        description (str): The text to display that explains what this finding type is about (and ideally how to fix it). This text will be the same for each concrete instance of the finding.
        enablement (constants.Enablement): Describes the default enablement setting for this finding type, used when it is added to the analysis profile.
"""

@auto_str
class MetricDescription(object):
    """Description of a metric type to be addded at configuration time.
    
    Args:
        metric_id (str): The globally unique metric id.
        display_name (str): The metric's name that is displayed in the UI.
        description (str): A description explaining what this metric means.
        group_id (str): the name of an analysis group under which the metric is placed (used to group the metrics in the analysis profile).
        aggregation (constants.MetricAggregation): How this metric is supposed to be aggregated up the directory hierarchy. Defaults to ``SUM``.
        value_type (constants.MetricValueType): Determines the metric's type. Defaults to ``NUMERIC``.
        properties (set[constants.MetricProperties]): Determines the metric's properties. This has effects on how/if the metric is displayed and assessed. Defaults to ``(SIZE_METRIC, )``. 
        """
    def __init__(self, metric_id, display_name, description, group_id, aggregation=MetricAggregation.SUM, value_type=MetricValueType.NUMERIC, properties=(MetricProperties.SIZE_METRIC,)):
        self.metricId = metric_id
        self.analysisGroup = group_id
        self.metricDefinition = {
            "name": display_name,
            "aggregation" : aggregation,
            "description" : description,
            "properties" : properties,
            "valueType" : value_type
        }

@auto_str
class MetricEntry(object):
    """A container for adding metric values to a file.
    
    Args:
        path (str): Path to a resource in Teamscale (usually a file). 
                    This can also point to architecture components using the following syntax: ``-architectures-/<architecture-name>/path/to/component/``
        metrics (dict[str, object]): A dictionary mapping from metric_id to metric value. The value depends on the metric type: Numeric: ``double``, Timestamp: ``int - unix timestamp in milliseconds``, Assessment: ``[<GREENVALUE>,<YELLOWVALUE>,<REDVALUE>]``
    """

    def __init__(self, path, metrics):
        self.path = path
        self.metrics = metrics

@auto_str
class NoneCodeMetricEntry(object):
    """A container for adding none code metrics to a project.
    
    Args:
        path (str): Arbitrary path to which the none-code metrics shall be attached  
        metrics (:class:`NoneCodeMetrics`): The metrics for this path 
    """
    def __init__(self, path, metrics):
        self.path = path
        self.metrics = metrics

@auto_str
class NoneCodeMetrics(object):
    """Container for none-code metric values.
    
    Args:
        content (str): The content displayed as content for the path
        count (int): The count value.
        assessment (dict[:class:`constants.AssessmentMetricColors`, int]): The assessment distribution for this path. 
        time (double): The time used to create this result (e.g. unit test run time, or build duration).
    """

    def __init__(self, content="", count=1, assessment={}, time=0.0):
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
        if(date is not None):
            self._set_date(date)

    def _get_date(self):
        return datetime.datetime.fromtimestamp(float(self._timestamp))

    def _set_date(self, date_object):
        import sys
        if sys.version_info > (3,):
            long_type = int
        else:
            long_type = long
        self.timestamp = long_type(time.mktime(date_object.timetuple())*1000)

    date = property(_get_date, _set_date)

class ServiceError(Exception):
    """Teamscale service returned an error."""
    pass
