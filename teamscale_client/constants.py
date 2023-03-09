"""This module contains multiple constants collections typically used when
communicating metrics and findings with Teamscale."""
from enum import Enum


class Assessment(str, Enum):
    """Constants to be used as assessment levels."""

    RED = "RED"

    ORANGE = "ORANGE"

    YELLOW = "YELLOW"

    GREEN = "GREEN"

    BASELINE = "BASELINE"

    UNKNOWN = "UNKNOWN"


class AssessmentMetricColors(str, Enum):
    """Constants used for colors in assessment metrics. """

    RED = "RED"

    YELLOW = "YELLOW"

    GREEN = "GREEN"


class Enablement(str, Enum):
    """The enablement describes which rating a finding should receive."""

    RED = "RED"
    """The finding should always be rated red."""

    YELLOW = "YELLOW"
    """The finding should always be rated yellow."""

    AUTO = "AUTO"
    """The assessment provided by the concrete finding is used."""

    OFF = "OFF"
    """The finding is disabled by default."""


class MetricAggregation(str, Enum):
    """Class that contains valid aggregation strategies."""

    SUM = "SUM"

    MAX = "MAX"

    MIN = "MIN"


class MetricValueType(str, Enum):
    """Metric value types."""

    NUMERIC = "NUMERIC"

    TIMESTAMP = "TIMESTAMP"

    ASSESSMENT = "ASSESSMENT"


class MetricProperties(str, Enum):
    """Possible properties used in metric definitions."""

    SIZE_METRIC = "SIZE_METRIC"
    """Normal number counting metric."""

    RATIO_METRIC = "RATIO_METRIC"
    """Metric is a percentage value between 0 and 1."""

    QUALITY_NEUTRAL = "QUALITY_NEUTRAL"
    """Quality neutral metrics can not be assessed/rated (e.g. number of files)"""

    LOW_IS_BAD = "LOW_IS_BAD"
    """Normally high values are considered bad, use this to inverse."""


class CoverageFormats(str, Enum):
    """Possible coverage formats that Teamscale can interpret."""

    CTC = "CTC"

    COBERTURA = "COBERTURA"

    GCOV = "GCOV"

    LCOV = "LCOV"

    XR_BABOON = "XR_BABOON"

    JACOCO = "JACOCO"

    DOT_COVER = "DOT_COVER"

    MS_COVERAGE = "MS_COVERAGE"

    VS_COVERAGE = "VS_COVERAGE"

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

    GOLANG_COVERAGE = "GOLANG_COVERAGE"

    LAUTERBACH_TRACE32 = "LAUTERBACH_TRACE32"

    TEAMSCALE_COMPACT_COVERAGE = "TEAMSCALE_COMPACT_COVERAGE"


class ReportFormats(str, Enum):
    """Report formats that Teamscale understands."""

    PCLINT = "PCLINT"

    CLANG = "CLANG"

    ASTREE = "ASTREE"

    FXCOP = "FXCOP"

    SPCOP = "SPCOP"

    CS_COMPILER_WARNING = "CS_COMPILER_WARNING"

    PYLINT = "PYLINT"

    FINDBUGS = "FINDBUGS"

    CPPCHECK = "CPPCHECK"

    MODEL_ADVISOR = "MODEL_ADVISOR"

    SAP_CODE_INSPECTOR = "SAP_CODE_INSPECTOR"

    PARASOFT_CPP_TEST = "PARASOFT_CPP_TEST"

    MYPY = "MYPY"

    JQASSISTANT = "JQASSISTANT"

    GENERIC_FINDINGS = "GENERIC_FINDINGS"


class UnitTestReportFormats(str, Enum):
    """Reports for unit test results that Teamscale understands."""

    JUNIT = "JUNIT"

    XUNIT = "XUNIT"

    MS_TEST = "MS_TEST"

    TESTWISE_COVERAGE = "TESTWISE_COVERAGE"

    NUNIT = "NUNIT"

    XCRESULT_JSON = "XCRESULT_JSON"


class ArchitectureFormats(str, Enum):
    """Architecture formats that Teamscale understands."""

    TEAMSCALE_ARCHITECTURE = "TEAMSCALE_ARCHITECTURE"

    FILE_LIST = "FILE_LIST"


class ConnectorType(str, Enum):
    """Connector types."""

    TFS = "Azure DevOps TFVC (TFS)"

    FILE_SYSTEM = "File System"

    MULTI_VERSION_FILE_SYSTEM = "Multi-Version File System"

    GIT = "Git"

    SVN = "Subversion"

    GERRIT = "Gerrit"


class TaskStatus(str, Enum):
    """Different statuses a task in Teamscale can have"""

    OPEN = "OPEN"

    RESOLVED = "RESOLVED"

    VERIFIED = "VERIFIED"

    DISCARDED = "DISCARDED"


class TaskResolution(str, Enum):
    """Different resolutions used in tasks"""
    NONE = "NONE"

    FIXED = "FIXED"

    INFEASIBLE = "INFEASIBLE"

    TOO_MUCH_EFFORT = "TOO_MUCH_EFFORT"
