import requests

from teamscale_client.data import ServiceError


class TeamscaleSession:
    """
    Syntactic sugar for easier session management with the with clause for uploading external data.
    This opens a session, returns a session_id and commits the session afterwards. Useful if one wants to upload
    multiple items in the same session. Otherwise, use 'auto-create' rather than this class.

    Examples:
        Use it in combination with the with statement:

        >>> with TeamscaleSession(base_url, timestamp, message, partition) as session_id:
        >>>     requests.post(...)
    """

    def __init__(self, url: str, timestamp: str, message: str, partition: str):
        """Initializes a new teamscale session

        Args:
            url: should look like /api/{version}/projects/{project}/external-analysis/session/
            timestamp: the processed timestamp from the client
            message: a message
            partition: the partitions
        """
        self.url = url
        self.timestamp = timestamp
        self.message = message
        self.partition = partition
        self.session_id = None

    def __enter__(self) -> str:
        """Creates a new session for uploading external data.

        Returns:
            a session_id which can be used to upload external data
        """
        response = requests.post(
            self.url,
            params={
                "t": self.timestamp,
                "message": self.message,
                "partition": self.partition
            }
        )
        if response.ok:
            self.session_id = response.text
            return self.session_id
        else:
            raise ServiceError(f"ERROR: POST {self.url}: {response.status_code}:{response.text}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes and Commits the Session."""
        response = requests.post(f"{self.url}/{self.session_id}")
        if response.ok:
            self.session_id = response.text
        else:
            raise ServiceError(f"ERROR: POST {self.url}: {response.status_code}:{response.text}")
