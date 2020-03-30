"""This module contains multiple constants collections typically used when
communicating metrics and findings with Teamscale."""

from __future__ import absolute_import
from __future__ import unicode_literals

class Assessment:
    """Constants to be used as assessment levels."""

    RED = "RED"

    YELLOW = "YELLOW"

class AssessmentMetricColors:
    """Constants used for colors in assessment metrics. """

    RED = "RED"

    YELLOW = "YELLOW"

    GREEN = "GREEN"

class Enablement:
    """The enablement describes which rating a finding should receive."""

    RED = "RED"
    """The finding should always be rated red."""

    YELLOW = "YELLOW"
    """The finding should always be rated yellow."""

    AUTO = "AUTO"
    """The assessment provided by the concrete finding is used."""

    OFF = "OFF"
    """The finding is disabled by default."""

class MetricAggregation:
    """Class that contains valid aggregation strategies."""

    SUM = "SUM"

    MAX = "MAX"

    MIN = "MIN"

class MetricValueType:
    """Metric value types."""

    NUMERIC = "NUMERIC"

    TIMESTAMP = "TIMESTAMP"

    ASSESSMENT = "ASSESSMENT"

class MetricProperties:
    """Possible properties used in metric definitions."""

    SIZE_METRIC = "SIZE_METRIC"
    """Normal number counting metric."""

    RATIO_METRIC = "RATIO_METRIC"
    """Metric is a percentage value between 0 and 1."""

    QUALITY_NEUTRAL = "QUALITY_NEUTRAL"
    """Quality neutral metrics can not be assessed/rated (e.g. number of files)"""

    LOW_IS_BAD = "LOW_IS_BAD"
    """Normally high values are considered bad, use this to inverse."""

class CoverageFormats:
    """Possible coverage formats that Teamscale can interpret."""

    CTC = "CTC"

    COBERTURA = "COBERTURA"

    GCOV = "GCOV"

    LCOV = "LCOV"

    XR_BABOON = "XR_BABOON"

    JACOCO = "JACOCO"
    
    DOT_COVER = "DOT_COVER"
    
    MS_COVERAGE = "MS_COVERAGE"
    
    ROSLYN = "ROSLYN"
    
    BULLSEYE = "BULLSEYE"

    SIMPLE = "SIMPLE"
    
    OPEN_COVER = "OPEN_COVER"
    
    IEC_COVERAGE = "IEC_COVERAGE"
    
    LLVM = "LLVM"
    
    CLOVER = "CLOVER"
    
    XCODE = "XCODE"
    
    TESTWISE_COVERAGE = "TESTWISE_COVERAGE"
    
    SAP_COVERAGE = "SAP_COVERAGE"
    
    ISTANBUL = "ISTANBUL"

class ReportFormats:
    """Report formats that Teamscale understands."""

    PCLINT = "PCLINT"
    
    CLANG = "CLANG"

    ASTREE = "ASTREE"

    FXCOP = "FXCOP"

    SPCOP = "SPCOP"

    CS_COMPILER_WARNING = "CS_COMPILER_WARNING"
   
    PYLINT = "PYLINT"

    FINDBUGS = "FINDBUGS"

class UnitTestReportFormats:
    """Reports for unit test results that Teamscale understands."""

    JUNIT = "JUNIT"

    XUNIT = "XUNIT"

class ConnectorType:
    """Connector types."""

    TFS = "Azure DevOps TFVC (TFS)"

    FILE_SYSTEM = "File System"

    MULTI_VERSION_FILE_SYSTEM = "Multi-Version File System"

    GIT = "Git"

    SVN = "Subversion"

    GERRIT = "Gerrit"

class TaskStatus:
    """Different statuses a task in Teamscale can have"""

    OPEN = "OPEN"

    RESOLVED = "RESOLVED"

    VERIFIED = "VERIFIED"

    DISCARDED = "DISCARDED"

class TaskResolution:
    """Different resolutions used in tasks"""
    NONE = "NONE"

    FIXED = "FIXED"

    INFEASIBLE = "INFEASIBLE"

    TOO_MUCH_EFFORT = "TOO_MUCH_EFFORT"
