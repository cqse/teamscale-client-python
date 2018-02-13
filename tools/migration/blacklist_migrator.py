#!/usr/bin/env python3
from migrator_base import MigratorBase, get_arguments


def main():
    BlacklistMigrator(*get_arguments()).migrate()


class BlacklistMigrator(MigratorBase):
    """ Class for migrating a blacklist between two instances.
    If some blacklisted finding cannot be found in the new instance, they will not
    be migrated.
    """
    def migrate(self):
        """ Migrates the blacklist. """
        blacklist_infos = self.get_blacklist_infos()
        if len(blacklist_infos) == 0:
            self.logger.info("No new blacklisted findings to migrate")
            exit(1)

        self.logger.info("Migrating %s blacklisted findings" % len(blacklist_infos))
        for blacklist_info in blacklist_infos:
            old_id = blacklist_info["findingId"]
            new_id = self.get_matching_finding_id(old_id)
            if new_id is None:
                self.logger.warning("Could not match finding %s to new instance" %
                                    self.get_findings_url(old_id))
            else:
                self.logger.info("Migrating blacklisted finding %s" % self.get_findings_url(old_id))
                self.blacklist_finding(blacklist_info, new_id)
            self.check_step()

        self.logger.info("Migrated %d/%d blacklisted findings" % (self.migrated, len(blacklist_infos)))

    def get_blacklist_infos(self):
        """ Returns all blacklist info objects from the old instance. """
        # Remove findings which have already been migrated and have the same id
        blacklisted_ids = set(self.get_from_old("finding-blacklist"))
        if len(blacklisted_ids) == 0:
            self.logger.info("Old instance does not have any blacklisted findings")
            exit(1)
        blacklisted_ids -= set(self.get_from_new("finding-blacklist"))

        infos = []
        for finding_id in blacklisted_ids:
            info = self.get_from_old("finding-blacklist", path_suffix=finding_id)
            if not info:
                self.logger.info("Blacklisted finding %s no longer exists at HEAD, not migrating" % finding_id)
            else:
                infos.append(info)
        return infos

    def blacklist_finding(self, blacklist_info, new_id):
        """ Blacklists a finding with the given id on the new instance. """
        self.migrated += 1
        blacklist_info["findingId"] = new_id
        self.put_in_new("finding-blacklist", blacklist_info, path_suffix=new_id)


if __name__ == "__main__":
    main()
