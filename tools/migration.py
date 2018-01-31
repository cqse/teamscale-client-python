from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
from teamscale_client import TeamscaleClient
from abc import ABC, abstractmethod

OLD_TEAMSCALE = {
    "url": "http://localhost:8080",
    "project": "old",
    "user": "user",
    "token": "tokentoken"
}

NEW_TEAMSCALE = {
    "url": "http://localhost:8080",
    "project": "new",
    "user": "user",
    "token": "tokentoken"
}


def main():
    client_new = TeamscaleClient(NEW_TEAMSCALE["url"],
                                 NEW_TEAMSCALE["user"],
                                 NEW_TEAMSCALE["token"],
                                 NEW_TEAMSCALE["project"])

    client_old = TeamscaleClient(OLD_TEAMSCALE["url"],
                                 OLD_TEAMSCALE["user"],
                                 OLD_TEAMSCALE["token"],
                                 OLD_TEAMSCALE["project"])

    BlacklistMigrator(client_old, client_new).migrate()
    TaskMigrator(client_old, client_new).migrate()


class MigratorBase(ABC):
    """ Base class for migrating data from one instance to another via REST calls. """

    def __init__(self, old, new):
        self.old = old
        self.new = new
        self.migrated = 0

    @staticmethod
    def get(client, service, path_param="", parameters=None):
        """ Performs a GET call from the client to the service with the given parameters
        and returns the response as a JSON Object.
        The path parameter are additions to the path, e.g /service/id.
        """
        response = client.get(client.get_project_service_url(service) + path_param, parameters)
        return json.loads(response.text)

    def get_from_old(self, service, path_param="", parameters=None):
        """ Performs a GET call with the given information on the instance from
        which the data should be migrated and returns the response as a JSON Object.
        """
        return self.get(self.old, service, path_param, parameters)

    def get_from_new(self, service, path_param="", parameters=None):
        """ Performs a GET call with the given information on the instance
        to which the data should be migrated and returns the response as a JSON Object.
        """
        return self.get(self.new, service, path_param, parameters)

    def put(self, service, data, path_param="", parameters=None):
        """ Performs a PUT call from the client to the service with the given parameters and data.
        The path parameter are additions to the path, e.g /service/id.
        """
        self.new.put(self.new.get_project_service_url(service) + path_param,
                     parameters=parameters,
                     json=data)

    def get_matching_finding_id(self, finding_id):
        """ Tries to find a matching finding in the new instance for
        the given findings id of the old instance.
        If no match could be found `None` is returned.
        """
        finding = self.get_from_old("findings-by-id", path_param=finding_id)
        new_findings = self.get_from_new("findings",
                                         path_param=finding["location"]["uniformPath"])
        for new_finding in new_findings:
            if self.match_finding(new_finding, finding):
                return new_finding["id"]
        return None

    @staticmethod
    def match_finding(finding1, finding2):
        """ Checks if the given two findings are the same. """
        if finding1["message"] != finding2["message"]:
            return False

        # some findings don't have a start line
        has_line1 = "rawStartLine" in finding1["location"]
        has_line2 = "rawStartLine" in finding2["location"]
        if has_line1 != has_line2:
            return False
        if not has_line1:
            return True
        return finding1["location"]["rawStartLine"] == finding2["location"]["rawStartLine"]

    @abstractmethod
    def migrate(self):
        pass


class BlacklistMigrator(MigratorBase):
    """ Class for migrating blacklists between two instances.
    If some blacklisted finding cannot be found in the new instance, they will not
    bet migrated.
    """

    def migrate(self):
        """ Migrates the blacklists. """
        migrate_blacklist = self.get_blacklist_infos()
        for blacklisted in migrate_blacklist:
            new_id = self.get_matching_finding_id(blacklisted["findingId"])
            if not new_id:
                print("could not find finding %s in new Teamscale" % blacklisted["findingId"])
            else:
                print("mapped old finding %s to new finding %s" % (blacklisted["findingId"], new_id))
                self.blacklist(blacklisted, new_id)

        if len(migrate_blacklist) == 0:
            print("No new blacklisted findings to migrate.")
        else:
            print("migrated %d/%d blacklisted findings" % (self.migrated, len(migrate_blacklist)))

    def get_blacklist_infos(self):
        """ Returns all blacklist info objects from the old instance. """
        # Remove findings which have already been migrated and have the same id
        blacklisted_ids = set(self.get_from_old("finding-blacklist")) - set(self.get_from_new("finding-blacklist"))

        infos = []
        for finding_id in blacklisted_ids:
            info = self.get_from_old("finding-blacklist", path_param=finding_id)
            if not info:
                print("Blacklisted finding %s no longer exists at HEAD, not migrating" % finding_id)
            else:
                infos.append(info)
        return infos

    def blacklist(self, blacklist_info, new_id):
        """ Blacklists a finding with the given id on the new instance. """
        self.migrated += 1
        blacklist_info["findingId"] = new_id
        self.put("finding-blacklist", blacklist_info, path_param=new_id)


class TaskMigrator(MigratorBase):
    """ Class for migrating tasks between two instances.
    Tasks will only be migrated if all connected findings are on the new instance as well.
    """

    def migrate(self):
        """ Migrates the tasks. """
        parameters = {"with-count": True, "max": 0}
        new_tasks_count = self.get_from_new("tasks", parameters=parameters)["totalTaskCount"] + 1

        old_tasks = self.get_from_old("tasks", parameters={"details": True})
        total = len(old_tasks)
        for old_task in old_tasks:
            if self.task_exists(old_task):
                total -= 1
            else:
                if self.adjust_task(old_task, new_tasks_count):
                    print("migrating task %s" % old_task["id"])
                    new_tasks_count += 1
                    self.add_task(old_task)
        if total == 0:
            print("No new tasks to migrate.")
        else:
            print("migrated %d/%d tasks" % (self.migrated, total))

    def adjust_task(self, task, new_id):
        """ Before adding the task to the new instance, it needs to get a new id, in order to prevent
        that potential existing tasks are overwritten. The ids of any connected findings need
        to be changed to the corresponding findings on the new instance, as well.
        If any finding cannot be matched on the new instance `False` will be returned, `True` otherwise."""
        for finding in task["findings"]:
            matching_finding_id = self.get_matching_finding_id(finding["findingId"])
            if not matching_finding_id:
                print("The finding %s for the task %s does not exists on the new instance." % (
                    finding["findingId"], task["id"]))
                return False
            finding["findingId"] = matching_finding_id
        task["id"] = new_id

        return True

    def add_task(self, task):
        """ Adds a task to the new instance """
        self.migrated += 1
        self.put("tasks", path_param=str(task["id"]), data=task)

    def task_exists(self, old_task):
        """ Checks if the given tasks already exists on the new instance. """
        new_tasks = self.get_from_new("tasks", parameters={
            "author": old_task["author"],
            "assignee": old_task["assignee"],
            "tags": old_task["tags"],
            "details": True
        })

        for new_task in new_tasks:
            if self.superficial_match(new_task, old_task) and self.task_findings_match(new_task, old_task):
                return True
        return False

    def task_findings_match(self, new, old):
        """ Checks if the findings of the given two tasks are the same. """
        new_findings = self.get_task_findings(self.new, new)
        old_findings = self.get_task_findings(self.old, old)

        for old_finding in old_findings:
            match_found = False
            for new_finding in new_findings:
                if self.match_finding(old_finding, new_finding):
                    match_found = True
                    break
            if not match_found:
                return False
        return True

    def superficial_match(self, task1, task2):
        """ A quick check if two tasks are roughly the same. It checks the contents of some fields and
        the number of findings.
        """
        return self.str_task(task1) == self.str_task(task2) and len(task1["findings"]) == len(task2["findings"])

    @staticmethod
    def str_task(task):
        """ Creates a simple string out of task with some of its field values. """
        return str([task[x] for x in ["subject", "description"]])

    def get_task_findings(self, client, task):
        """ Returns the findigs objects for a task (if it has any) """
        findings = []
        for entry in task["findings"]:
            findings.append(self.get(client, "findings-by-id", path_param=entry["findingId"]))
        return findings


if __name__ == "__main__":
    main()
