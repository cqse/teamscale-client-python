# 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests

import datetime
import os
import sys
import re

from teamscale_client import TeamscaleClient


TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "build"
ACCESS_TOKEN = "ide-access-token"


def confirm(prompt=None, resp=False):
    """prompts for yes or no response from the user. Returns True for yes and
    False for no.

    'resp' should be set to the default value assumed by the caller when
    user simply types ENTER.

    >>> confirm(prompt='Create Directory?', resp=True)
    Create Directory? [y]|n:
    True
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y:
    False
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: y
    True

    """

    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

    while True:
        ans = input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False


def determine_stale_dashboards(active_projects, client):
    """Determines dashboards that have no reference to active projects.

        Args:
            active_projects: Set of active projects
            client: TeamscaleClient

        Returns:
            Set of dashboard ids that do not refer to any active project.
        """
    stale_dashboards=[]
    for dashboard in client.get_all_dashboard_details():
        dashboard_name = '%s/%s' % (dashboard['owner'], dashboard['name'])
        referenced_projects = set(re.findall('"project": "([a-zA-Z0-9_]+)"', dashboard['descriptorJSON']))
        if active_projects.isdisjoint(referenced_projects):
            print("Dashboard %s only references projects %s (none of which is active anymore)"
                  % (dashboard_name, referenced_projects))
            stale_dashboards.append(dashboard_name)
    return stale_dashboards


def main():
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, "")
    active_projects = set([x.id for x in client.get_projects()])
    print('active project IDs:', active_projects)

    dashboards_to_be_removed = determine_stale_dashboards(active_projects, client)

    for dashboard in dashboards_to_be_removed:
        if confirm('really delete dashboard %s ?'%dashboard):
            print(client.delete_dashboard(dashboard))


if __name__ == '__main__':
    main()
