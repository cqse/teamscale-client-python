#!/usr/bin/env python3
from migration.migrator_base import MigratorBase, get_arguments


def main():
    """ Migrates the task from the old instance to the new one.
    It automatically reads the arguments from the command line. """
    (config, debug) = get_arguments()
    TaskMigrator(config, debug).migrate()


class TaskMigrator(MigratorBase):
    """ Class for migrating tasks between two instances.
    Tasks will only be migrated if all connected findings are on the new instance as well.
    """
    def migrate(self):
        """ Migrates the tasks. """
        old_tasks = self.get_filtered_tasks()
        for old_task in old_tasks:
            old_task_id = old_task["id"]
            if self.adjust_task(old_task):
                self.logger.info("Migrating task %s" % self.get_tasks_url(old_task_id))
                self.add_task(old_task)

        if len(old_tasks) == 0:
            self.logger.info("No new tasks to migrate.")
        else:
            self.logger.info("Migrated %d/%d tasks" % (self.migrated, len(old_tasks)))

    def get_filtered_tasks(self):
        """ Returns a list comprising of the tasks of the old instance which are not yet
         migrated to the new instance.
         """
        old_tasks = self.get_from_old("tasks", parameters={"details": True})
        return list(filter(lambda task: not self.task_exists(task), old_tasks))

    def adjust_task(self, task):
        """ Before adding the task to the new instance the ids of any connected findings need
        to be changed to the corresponding findings on the new instance.
        If any finding cannot be matched on the new instance `False` will be returned, `True` otherwise.
        """
        for finding in task["findings"]:
            matching_finding_id = self.get_matching_finding_id(finding["findingId"])
            if matching_finding_id is None:
                self.logger.warn("The finding %s for the task %s does not exists on the new instance." % (
                    self.get_findings_url(self.old, finding["findingId"]), task["id"]))
                return False
            finding["findingId"] = matching_finding_id
        # If the id is 0, the backend will assign a valid new id
        task["id"] = 0
        return True

    def get_tasks_url(self, task_id, client=None):
        """ Creates a url of the old instance to the task with the given id. """
        if client is None:
            client = self.old
        return "{0.url}/tasks.html#details/{0.project}/?id={1}".format(client, task_id)

    def add_task(self, task):
        """ Adds a task to the new instance """
        self.migrated += 1
        self.put_in_new("tasks", path_suffix=str(task["id"]), data=task)

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

    def task_findings_match(self, new_task, old_task):
        """ Checks if the findings of the given two tasks are the same.
        Returns True if they are, False otherwise.
        """
        new_findings = self.get_task_findings(self.new, new_task)
        old_findings = self.get_task_findings(self.old, old_task)

        for old_finding in old_findings:
            if not self.finding_match_in_list(old_finding, new_findings):
                return False
        return True

    def finding_match_in_list(self, finding, finding_list):
        """ Checks whether there is a match for a finding in a list of findings. """
        for new_finding in finding_list:
            if self.match_finding(finding, new_finding):
                return True
        return False

    def superficial_match(self, task1, task2):
        """ A quick check if two tasks are roughly the same. It checks the contents of some fields and
        the number of findings.
        """
        return self.task_to_list(task1) == self.task_to_list(task2) and len(task1["findings"]) == len(task2["findings"])

    @staticmethod
    def task_to_list(task):
        """ Creates a simple string out of task with some of its field values. """
        return [task[x] for x in ["subject", "description"]]

    def get_task_findings(self, client, task):
        """ Returns the findings objects for a task (if it has any) """
        findings = []
        for entry in task["findings"]:
            findings.append(self.get(client, "findings-by-id", path_suffix=entry["findingId"]))
        return findings


if __name__ == "__main__":
    main()
