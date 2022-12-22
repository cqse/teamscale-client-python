import argparse
import json
import logging
import urllib.parse
import sys

from teamscale_client import TeamscaleClient
from pathlib import Path


def main():
    instance, group_desc = get_config_data()
    teamscale = TeamscaleClient(**instance)

    group_id = urllib.parse.quote(group_desc["groupName"])
    url = teamscale.get_global_service_url("external-findings-groups")
    teamscale.put(url+group_id, group_desc)
    print("Successfully uploaded group description from `%s`" % sys.argv[2])


def get_config_data():
    """ Parses the arguments for the migration tool. """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("config", help="The path to the config file. Needs to be in a specific format, "
                                       "see config.template.")
    parser.add_argument("descriptions", help="The findings descriptions")
    args = parser.parse_args()
    return load_json(args.config), load_json(args.descriptions)


def load_json(path):
    """ Loads the config data as a JSON and returns it. """
    json_file = Path(path)
    if json_file.exists():
        try:
            return json.load(json_file.open())
        except json.JSONDecodeError:
            logging.getLogger().exception("Config file '%s' is malformed" % path, exc_info=True)
    else:
        logging.getLogger().exception("Config file '%s' does not exist" % path)
    exit(1)


if __name__ == "__main__":
    main()