class Assessment:
    """Constants to be used as assessment levels."""

    RED = "RED"

    YELLOW = "YELLOW"

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

