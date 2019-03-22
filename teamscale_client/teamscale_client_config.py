from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from configparser import ConfigParser
import os


# Name of the default Teamscale client configuration file.
TEAMSCALE_CLIENT_CONFIG_FILENAME = '.teamscale-client.config'


class TeamscaleClientConfig:
    """Configuration parameters for connections to Teamscale

    In order to configure a Teamscale client, the config file must at least provide the following entries:
    * `url`: The url of the Teamscale server.
    * `username`: The username to use to perform API calls
    * `access_token`: The access token to use.

    The config file can also specify a project `id`.
    If no project `id` is specified, '' is used in case `project_required` is `False`.
    A `TeamscaleClient` created using a configuration without project `id` will only perform global calls.
    """

    def __init__(self, url, username, access_token, project=''):
        """Constructor."""
        self.url = url
        self.username = username
        self.access_token = access_token
        self.project_id = project
        self.config_file = None

    @staticmethod
    def from_config_file(config_file):
        """Reads a Teamscale client configuration from the specified file.

        Args:
            config_file (str): Path of the client configuration to use.
        """
        if not os.path.exists(config_file) or not os.path.isfile(config_file):
            raise RuntimeError('Config file could not be found: %s' % config_file)

        parser = ConfigParser()
        parser.read(config_file)

        url = parser.get('teamscale', 'url', fallback=None)
        username = parser.get('teamscale', 'username', fallback=None)
        access_token = parser.get('teamscale', 'access_token', fallback=None)
        project_id = parser.get('project', 'id', fallback='')

        config = TeamscaleClientConfig(url, username, access_token, project_id)
        config.config_file = config_file
        return config

    @staticmethod
    def from_config_file_in_home_dir():
        """Reads a Teamscale client configuration from the user home dir.
        The configuration file must be named as in `TEAMSCALE_CLIENT_CONFIG_FILENAME`.
        """
        home = os.path.expanduser("~")
        config_file = os.sep.join([home, TEAMSCALE_CLIENT_CONFIG_FILENAME])
        return TeamscaleClientConfig.from_config_file(config_file)

    def overwrite_with(self, other):
        """Overwrites values in this configuration with values from the other configuration.
        This is useful to combine multiple configurations from different files, e.g. the home dir and the
        repository root.
        """
        if other.url:
            self.url = other.url
        if other.username:
            self.username = other.username
        if other.access_token:
            self.access_token = other.access_token
        if other.project_id:
            self.project_id = other.project_id
        if other.config_file:
            self.config_file = other.config_file

    def is_sufficient(self, require_project_id=False):
        teamscale_configured = self.access_token and self.username and self.url
        if not teamscale_configured:
            return False
        if not require_project_id:
            return True
        return True if self.project_id else False
