import argparse
import json

from pathlib import Path
from task_migrator import TaskMigrator
from blacklist_migrator import BlacklistMigrator
from migrator_base import create_logger


def main():
    """ Migrates the blacklists and tasks of multiple projects from one server to the projects to the other.
    It automatically reads the arguments from the command line. """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("config", help="The path to the config file. Needs to be in a specific format, "
                                       "see batch_config.template.")
    args = parser.parse_args()
    logger = create_logger()
    config_file = Path(args.config)
    if not config_file.exists():
        logger.error("Config file does not exist")

    with config_file.open() as file:
        data = json.load(file)
        base_config = {x: data[x] for x in ["old_instance", "new_instance"]}

        for mapping in data["project_mappings"]:
            migrate(base_config, mapping, logger)


def migrate(base_config, mapping, logger):
    """ Migrates the blacklist and the tasks of between the projects defined in the mapping.
    The servers containing the project are defined in the base config.
    """
    if not all(key in mapping for key in ("from", "to")):
        logger.error("Project mapping is malformed: %s" % mapping)
        return None

    base_config["old_instance"]["project"] = mapping["from"]
    base_config["new_instance"]["project"] = mapping["to"]

    logger.info("Migrating from '{from}' to '{to}'".format(**mapping))
    BlacklistMigrator(base_config).migrate()
    TaskMigrator(base_config).migrate()


if __name__ == "__main__":
    main()
