from teamscale_client import TeamscaleClient
from teamscale_client.data import ProjectConfiguration, FileSystemSourceCodeConnectorConfiguration, \
    GitSourceCodeConnectorConfiguration, MultiVersionFileSystemSourceCodeConnectorConfiguration, \
    TFSSourceCodeConnectorConfiguration, SubversionSourceCodeConnectorConfiguration

TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
ACCESS_TOKEN = "ide-access-token"

PROJECT_ID = "test"

ANALYSIS_PROFILE = "Python (default)"
INCLUDE_PATTERN = "**.py"

LOCAL_PATH = "/path/to/folder"
LOCAL_PATH_MULTIVERSION = "/path/to/folder"
ACCOUNT_NAME_GIT = "account_git"
ACCOUNT_NAME_TFS = "account_tfs"
ACCOUNT_NAME_SVN = "account_svn"


def show_projects(client):
    projects = client.get_projects()
    print([str(project) for project in projects])


def create_project_with_file_system_connector():
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH,
                                                                    repository_identifier="Local",
                                                                    included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project", project_id="test-project",
                                                 profile=ANALYSIS_PROFILE, connectors=[file_system_config])
    client.create_project(project_configuration)


def update_project_with_file_system_connector():
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH,
                                                                    repository_identifier="Local",
                                                                    included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project", project_id="test-project",
                                                 profile=ANALYSIS_PROFILE, connectors=[file_system_config],
                                                 alias="teamscale_python_client")
    client.update_project(project_configuration)


def create_project_with_git_connector():
    git_config = GitSourceCodeConnectorConfiguration(default_branch_name="master", account=ACCOUNT_NAME_GIT,
                                                     repository_identifier="Git", included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project 2", project_id="test-project-002",
                                                 profile=ANALYSIS_PROFILE, connectors=[git_config])
    client.create_project(project_configuration)


def create_project_with_multiversion_file_system_connector():
    mvfsc_config = MultiVersionFileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH_MULTIVERSION,
                                                                          repository_identifier="Local-Multiversion",
                                                                          included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project 3", project_id="test-project-003",
                                                 profile=ANALYSIS_PROFILE, connectors=[mvfsc_config])
    client.create_project(project_configuration)


def create_project_with_tfs_connector():
    tfs_config = TFSSourceCodeConnectorConfiguration(account=ACCOUNT_NAME_TFS, repository_identifier="TFS",
                                                     included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project 4", project_id="test-project-004",
                                                 profile=ANALYSIS_PROFILE, connectors=[tfs_config])
    client.create_project(project_configuration)


def create_project_with_svn_connector():
    svn_config = SubversionSourceCodeConnectorConfiguration(account=ACCOUNT_NAME_SVN, repository_identifier="SVN",
                                                            included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name="Test Project 5", project_id="test-project-005",
                                                 profile=ANALYSIS_PROFILE, connectors=[svn_config])
    client.create_project(project_configuration)


if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, ACCESS_TOKEN, PROJECT_ID)
    show_projects(client)

    create_project_with_file_system_connector()
    show_projects(client)

    update_project_with_file_system_connector()
    show_projects(client)

    create_project_with_git_connector()
    show_projects(client)

    create_project_with_multiversion_file_system_connector()
    show_projects(client)

    create_project_with_tfs_connector()
    show_projects(client)

    create_project_with_svn_connector()
    show_projects(client)
