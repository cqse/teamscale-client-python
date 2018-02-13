#!/usr/bin/env python3
from migrator_base import MigratorBase, get_arguments
from teamscale_client.data import ServiceError


def main():
    """ Migrates the task from the old instance to the new one.
    It automatically reads the arguments from the command line. """
    TaskMigrator(*get_arguments()).migrate()


class TaskMigrator(MigratorBase):
    """ Class for migrating tasks between two instances.
    Tasks will only be migrated if all connected findings are on the new instance as well.
    """
    def migrate(self):
        """ Migrates the tasks. """
        old_tasks = self.get_from_old("tasks", parameters={"details": True})
        if len(old_tasks) == 0:
            self.logger.info("No new tasks to migrate.")
            exit(1)

        self.logger.info("Migrating %s tasks" % len(old_tasks))
        for old_task in old_tasks:
            old_task_id = old_task["id"]
            self.adjust_task(old_task)
            self.logger.info("Migrating task %s" % self.get_tasks_url(old_task_id))
            self.add_task(old_task)
            self.check_step()
        self.logger.info("Migrated %d/%d tasks" % (self.migrated, len(old_tasks)))

    def adjust_task(self, task):
        """ Before adding the task to the new instance the ids of any connected findings need
        to be changed to the corresponding findings on the new instance.
        """
        for finding in task["findings"]:
            matching_finding_id = self.get_matching_finding_id(finding["findingId"])
            if matching_finding_id is None:
                self.logger.warn("The finding %s for the task %s does not exists on the new instance." % (
                    self.get_findings_url(finding["findingId"]), task["id"]))
            else:
                finding["findingId"] = matching_finding_id

    def get_tasks_url(self, task_id, client=None):
        """ Creates a url of the old instance to the task with the given id. """
        if client is None:
            client = self.old
        return "{0.url}/tasks.html#details/{0.project}/?id={1}".format(client, task_id)

    def add_task(self, task):
        """ Adds a task to the new instance """
        self.migrated += 1
        self.put_in_new("tasks", path_suffix=str(task["id"]), data=task)

    def get_task_findings(self, client, task):
        """ Returns the findings objects for a task (if it has any) """
        findings = []
        for entry in task["findings"]:
            finding = self.get_finding_by_id(client, entry["findingId"])
            if finding is None:
                continue
            findings.append(finding)
        return findings


if __name__ == "__main__":
    main()
