import json
import argparse
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from teamscale_client import TeamscaleClient
from teamscale_client.data import ServiceError
from requests.exceptions import ConnectionError

# TODO: migrating between different versions (messages might change)


def get_arguments():
    """ Parses the arguments for the migration tool. """
    parser = argparse.ArgumentParser(description="test", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("config", help="The path to the config file. Needs to be in a specific format, "
                                       "see config.template.")
    parser.add_argument("--debug", action="store_true", help="The debug option which enables debug log. Can be use to "
                                                             "dry-run the migration, as it does not change anything.")
    return parser.parse_args()


class MigratorBase(ABC):
    """ Base class for migrating data from one instance to another via REST calls. """

    def __init__(self):
        args = get_arguments()
        self.debug = args.debug
        self.logger = self.get_logger()
        self.old, self.new = self.load_config(args.config)
        self.migrated = 0
        self.cache = {}

        if self.debug:
            self.logger.debug("Debug Mode ON")

    def load_config(self, config_path):
        """ Reads the given config defined by its path and creates the two teamscale clients from it.
        One old instance (migrating from) and a new onoe (migrating to).
        """
        config_file = Path(config_path)
        if config_file.exists():
            try:
                data = json.load(config_file.open())
                return self.get_client(data["old_instance"]), self.get_client(data["new_instance"])
            except (json.JSONDecodeError, KeyError) as e:
                self.logger.exception("Config file '%s' is malformed" % config_path, exc_info=True)
            except ConnectionError as e:
                self.logger.exception("Connection to %s could not be established" % e.request.url)
            except ServiceError as e:
                self.logger.exception("Creating the teamscale clients failed.")
        else:
            self.logger.exception("Config file '%s' does not exist" % config_path)
        exit(1)

    @staticmethod
    def get_client(data):
        """ Creates a teamscale client from the given data """
        return TeamscaleClient(data["url"], data["user"], data["token"], data["project"])

    def get_logger(self):
        """ Creates a logger """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if self.debug:
            logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)-8s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def check_cache(self, request, use_cache):
        """ If use_cache is True it checks if the cache already contains the response
        for the given request and returns it.
        If the cache shouldn't be used or no cache was found None is returned.
        """
        request = str(request)
        if use_cache and (request in self.cache):
            self.logger.debug("Cache hit for %s" % request)
            return self.cache[request]
        return None

    def cache_request(self, request, response, use_cache):
        """ If the cache should be used, the request and its response are cached. """
        if use_cache:
            self.cache[str(request)] = response

    def get(self, client, service, path_suffix="", parameters=None, use_cache=True):
        """ Performs a GET call from the client to the service with the given parameters
        and returns the response as a JSON Object.
        Args:
            path_suffix(str): Will be added to the end of the project service URL
        """
        url = client.get_project_service_url(service) + path_suffix

        response = self.check_cache((url, parameters), use_cache)
        if response is None:
            try:
                self.logger.debug("Service Call: {}".format((url, parameters)))
                response = client.get(url, parameters).json()
            except ServiceError as e:
                self.logger.exception("Fetching data from %s failed (%s)" % (url, e.response.status_code))
                exit(1)
        self.cache_request((url, parameters), response, use_cache)
        return response

    def get_from_old(self, service, path_suffix="", parameters=None, use_cache=True):
        """ Performs a GET call with the given information on the instance from
        which the data should be migrated and returns the response as a JSON Object.
        Args:
            path_suffix(str): Will be added to the end of the project service URL
        """
        return self.get(self.old, service, path_suffix, parameters, use_cache)

    def get_from_new(self, service, path_suffix="", parameters=None, use_cache=True):
        """ Performs a GET call with the given information on the instance
        to which the data should be migrated and returns the response as a JSON Object.
        Args:
            path_suffix(str): Will be added to the end of the project service URL
        """
        return self.get(self.new, service, path_suffix, parameters, use_cache)

    def put_in_new(self, service, data, path_suffix="", parameters=None):
        """ Performs a PUT call from the client to the service with the given parameters and data.
        The path parameter are additions to the path, e.g /service/id.
        Args:
            path_suffix(str): Will be added to the end of the project service URL
        """
        if not self.debug:
            self.new.put(self.new.get_project_service_url(service) + path_suffix,
                         parameters=parameters,
                         json=data)

    def get_matching_finding_id(self, finding_id):
        """ Tries to find a matching finding in the new instance for
        the given findings id of the old instance.
        If no match could be found `None` is returned.
        """
        finding = self.get_from_old("findings-by-id", path_suffix=finding_id)
        new_findings = self.get_from_new("findings", path_suffix=finding["location"]["uniformPath"])
        for new_finding in new_findings:
            if self.match_finding(new_finding, finding):
                return new_finding["id"]
        return None

    def get_findings_url(self, findings_id, client=None):
        """ Creates a url link to the finding with the given id on the given Teamscale """
        if client is None:
            client = self.old
        return "{0.url}/findings.html#details/{0.project}/?id={1}".format(client, findings_id)

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
        """ Migrates the date from the old instance to the new one """
        pass
