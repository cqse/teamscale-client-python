from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from configparser import ConfigParser

class TeamscaleClientConfig:
    """Configuration parameters for connections to Teamscale"""

    def __init__(self, config_file):
        """Reads a Teamscale configuration from the specified file.

        The config file must at least provide the following entries:
        * `url`: The url of the Teamscale server.
        * `username`: The username to use to perform API calls
        * `access_token`: The access token to use.

        The config file can also specify a project `id`. If no project `id` is specified, '' is used.
        A `TeamscaleClient` created using a configuration without project `id` will only perform global calls.
        """
        parser = ConfigParser()
        parser.read(config_file)

        self.url = parser.get('teamscale', 'url')
        self.username = parser.get('teamscale', 'username')
        self.access_token = parser.get('teamscale', 'access_token')
        self.project_id = parser.get('project', 'id', fallback='')
