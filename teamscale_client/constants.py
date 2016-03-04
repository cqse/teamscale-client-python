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