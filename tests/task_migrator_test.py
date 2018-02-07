from __future__ import absolute_import
from __future__ import unicode_literals

import responses
from tools.migration.task_migrator import TaskMigrator
from test_utils import get_global_service_mock
from copy import deepcopy

URL = "http://localhost:8080"
CONFIG = {
    "old_instance": {
        "url": URL,
        "project": "old",
        "user": "admin",
        "token": "token"
    },
    "new_instance": {
        "url": URL,
        "project": "new",
        "user": "admin",
        "token": "token"
    }
}


class TestTaskMigrator:
    """ Simple class for bundling the test for the task migration. """
    @staticmethod
    def get_migrator(config):
        """
        Returns a task migrator with the given config.
        For an example config look at CONFIG
        """
        TestTaskMigrator.create_necessary_client_responses(URL)
        return TaskMigrator(config, False)

    @staticmethod
    def create_necessary_client_responses(url, version=40000):
        """ Creates responses which are necessary to create a client """
        responses.add(responses.GET, get_global_service_mock(url, "service-api-info"),
                      status=200, content_type="application/json", body='{ "apiVersion": 3 }')
        responses.add(responses.GET, get_global_service_mock(url, "health-metrics"),
                      status=200, content_type="text/plain", body="version %s 0" % version)

    def get_default_migrator(self):
        """ Returns the migrator with the default settings """
        return self.get_migrator(CONFIG)

    @responses.activate
    def test_different_versions(self, caplog):
        """ Tests the case where we want to migrate between two TS-instances with a different
        version. A warning should be logged and the version_match flag should be False.
        """
        config = deepcopy(CONFIG)
        new_url = "http://localhost:8081"
        config["new_instance"]["url"] = new_url
        self.create_necessary_client_responses(new_url, version=30000)
        migrator = self.get_migrator(config)

        warning = list(filter(lambda x: x.levelname == "WARNING" and "version" in x.message, caplog.records))
        assert len(warning) == 1, "Missing warning about version mismatch"
        assert not migrator.versions_match, "Flag 'versions_match' should be False"
