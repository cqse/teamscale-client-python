import time


def get_timestamp_parameter(timestamp, branch=None):
    """Returns the timestamp parameter. Will use the branch parameter if it is set.
    Returned timestamp is 'HEAD' if given timestamp is `None`.

    Args:
        timestamp (datetime.datetime): The timestamp to convert
        branch (str): The branch to use. If this parameter is not set, the branch that was used to initialize the
                      client is used, if any.

    Returns:
        str: timestamp in ms, optionally prepended by the branch name.
        Returned timestamp is 'HEAD' if given timestamp is `None`.
    """
    timestamp_or_head = 'HEAD'
    if timestamp:
        timestamp_seconds = time.mktime(timestamp.timetuple())
        timestamp_or_head = str(int(timestamp_seconds * 1000))
    default_branch_name = branch
    if default_branch_name:
        return default_branch_name + ":" + timestamp_or_head
    return timestamp_or_head
