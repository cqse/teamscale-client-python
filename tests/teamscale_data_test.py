from teamscale_client.data import Finding
from teamscale_client.constants import Assessment


def test_finding_compare_1():
    """Checks if comparison for equality succeeds"""
    f1 = Finding("1A1837926D5406B9B33DDB84A1383525", "No message at all", Assessment.YELLOW, start_line=100)
    f2 = Finding("1A1837926D5406B9B33DDB84A1383525", "No message at all", Assessment.YELLOW, start_line=100)

    assert f1 == f2
    assert f1 <= f2
    assert f1 >= f2


def test_finding_compare_2():
    """Checks if comparison for ordering succeeds"""
    f1 = Finding("1A1837926D5406B9B33DDB84A1383525", "No message at all", Assessment.YELLOW, start_line=100)
    f2 = Finding("2A1837926D5406B9B33DDB84A1383525", "No message at all", Assessment.YELLOW, start_line=200)

    assert f1 != f2
    assert f1 < f2
    assert f2 > f1
