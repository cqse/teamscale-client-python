#!/usr/bin/env python3
from teamscale_client.constants import TaskStatus

from tools.migration.migrator_base import MigratorBase, get_arguments


def main():
    """ Migrates the task from the old instance to the new one.
    It automatically reads the arguments from the command line. """
    TaskMigrator(*get_arguments()).migrate()


class TaskMigrator(MigratorBase):
    """ Class for migrating tasks between two instances.
    Tasks will only be migrated if all connected findings are on the new instance as well.
    """
    def __init__(self, config_data, debug=False, dry_run=False, step_by_step=False, overwrite_tasks=True,
                 findings_timestamp=None, get_findings_timestamp_from_task_creation=False, overwrite_tasks_offset=0):
        super().__init__(config_data, debug=debug, dry_run=dry_run, step_by_step=step_by_step)
        self.overwrite_tasks = overwrite_tasks
        self.findings_timestamp = findings_timestamp
        self.get_findings_timestamp_from_task_creation = get_findings_timestamp_from_task_creation
        self.overwrite_tasks_offset = overwrite_tasks_offset

    def migrate(self):
        """ Migrates the tasks. """
        old_tasks = self.get_from_old("tasks", parameters={"details": True})
        if len(old_tasks) == 0:
            self.logger.info("No new tasks to migrate.")
            exit(0)

        self.logger.info("Migrating %s tasks" % len(old_tasks))
        for old_task in old_tasks:
            old_task_id = old_task["id"]
            self.logger.debug('Working on task %i (%s)' % (old_task_id, old_task["status"]))
            if not self.filter_task(old_task):
                self.logger.debug('Skipping task %i (%s)' % (old_task_id, old_task["status"]))
                continue
            self.adjust_task(old_task)
            self.pre_process_task(old_task)
            self.logger.info("Migrating task %s" % self.get_tasks_url(old_task_id))
            new_task_id = self.add_task(old_task)
            self.post_process_task(old_task, old_task_id, new_task_id)
            self.check_step()

        self.logger.info("Migrated %d/%d tasks" % (self.migrated, len(old_tasks)))

    def adjust_task(self, task):
        """ Before adding the task to the new instance the ids of any connected findings need
        to be changed to the corresponding findings on the new instance.
        """
        self.logger.debug('Adjusting %i findings' % len(task["findings"]))

        timestamp_for_finding_on_new_instance = self.findings_timestamp
        if self.get_findings_timestamp_from_task_creation:
            timestamp_for_finding_on_new_instance = task["created"]

        for finding in task["findings"]:
            self.logger.debug('Searching for finding %s' % finding["findingId"])

            matching_finding_id = self.get_matching_finding_id(finding["findingId"], timestamp_for_finding_on_new_instance)
            if matching_finding_id is None:
                self.logger.warn("The finding %s for task %s does not exists on the new instance." % (
                    self.get_findings_url(finding["findingId"]), task["id"]))
            else:
                self.logger.debug("Found finding %s for task %s on new instance: %s." % (
                    self.get_findings_url(finding["findingId"]), task["id"],
                    self.get_findings_url(matching_finding_id, client=self.new)))
                finding["findingId"] = matching_finding_id

    def filter_task(self, task):
        """Additional task filter. Default implementation does nothing."""
        return True

    def pre_process_task(self, task):
        """Additional task preprocessing. Default implementation does nothing."""
        pass

    def post_process_task(self, task, old_task_id, new_task_id):
        """Additional task postprocessing. Default implementation does nothing."""
        pass

    def get_tasks_url(self, task_id, client=None):
        """ Creates a url of the old instance to the task with the given id. """
        if client is None:
            client = self.old
        return "{0.url}/tasks.html#details/{0.project}/?id={1}".format(client, task_id)

    def add_task(self, task):
        """ Adds a task to the new instance """
        self.migrated += 1
        path_suffix = str(task["id"] + self.overwrite_tasks_offset) if self.overwrite_tasks else '0'
        new_task_response = self.put_in_new("tasks", path_suffix=path_suffix, data=task)
        new_task_id = new_task_response.json() if new_task_response else 100000
        if task["status"] != TaskStatus.OPEN:
            # Need to put it a second time to get the status right
            self.put_in_new("tasks", path_suffix=str(new_task_id), data=task)
        return new_task_id


if __name__ == "__main__":
    main()
