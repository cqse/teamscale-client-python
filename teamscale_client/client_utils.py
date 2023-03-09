from packaging import version


def parse_version(version_element):
    """Parses a version number from a given json dictionary from teamscale.

    Args:
        version_element (str | dict): dictionary of major, minor and patch number

    Returns:
        a version number

    """
    if isinstance(version_element, dict):
        version_element = "{major}.{minor}.{patch}".format(**version_element)
    return version.parse(version_element)
