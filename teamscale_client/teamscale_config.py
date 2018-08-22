from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

class TeamscaleConfig:
    """Configuration parameters for connections to Teamscale"""
    def __init__(self, url, username, access_token, project_id):
        """Constructor
        """
        self.url = url
        self.username = username
        self.access_token = access_token
        self.project_id = project_id
