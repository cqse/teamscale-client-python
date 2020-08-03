from __future__ import print_function

import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models import ProjectConfiguration
from util.additional_model import FileSystemSourceCodeConnectorConfiguration
from util.additional_model import GitSourceCodeConnectorConfiguration
from util.additional_model import MultiVersionFileSystemSourceCodeConnectorConfiguration
from util.additional_model import TFSSourceCodeConnectorConfiguration
from util.additional_model import SubversionSourceCodeConnectorConfiguration

USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-token'
TEAMSCALE_URL = 'http://localhost:8080'

ANALYSIS_PROFILE = 'Python (default)'
INCLUDE_PATTERN = '**.py'
LOCAL_PATH = '/path/to/folder'
LOCAL_PATH_MULTIVERSION = '/path/to/folder'
TFS_PATH_SUFFIX = '$/Data/Dev/Main/Source/project'

ACCOUNT_NAME_GIT = 'account_git'
ACCOUNT_NAME_TFS = 'account_tfs'
ACCOUNT_NAME_SVN = 'account_svn'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)


def show_projects():
    projects = client.get_all_projects()
    print([str(project) for project in projects])


def create_project_with_file_system_connector():
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH,
                                                                    repository_identifier='Local',
                                                                    included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name='Test Project', id='test-project',
                                                 profile=ANALYSIS_PROFILE, connectors=[file_system_config])
    client.create_project(project_configuration=project_configuration)


def update_project_with_file_system_connector():
    file_system_config = FileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH,
                                                                    repository_identifier='Local',
                                                                    included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name='Test Project', id='test-project',
                                                 profile=ANALYSIS_PROFILE, connectors=[file_system_config],
                                                 alias='Teamscale Python Client')
    client.edit_project1(project='test-project', project_configuration=project_configuration)


def create_project_with_git_connector():
    git_config = GitSourceCodeConnectorConfiguration(default_branch_name='main', account=ACCOUNT_NAME_GIT,
                                                     repository_identifier='Git', included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name='Test Project 2', id='test-project-002',
                                                 profile=ANALYSIS_PROFILE, connectors=[git_config])
    client.create_project(project_configuration=project_configuration)


def create_project_with_multiversion_file_system_connector():
    mvfsc_config = MultiVersionFileSystemSourceCodeConnectorConfiguration(input_directory=LOCAL_PATH_MULTIVERSION,
                                                                          repository_identifier='Local-Multiversion',
                                                                          included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name='Test Project 3', id='test-project-003',
                                                 profile=ANALYSIS_PROFILE, connectors=[mvfsc_config])
    client.create_project(project_configuration=project_configuration)


def create_project_with_tfs_connector():
    tfs_config = TFSSourceCodeConnectorConfiguration(account=ACCOUNT_NAME_TFS, repository_identifier='TFS',
                                                     included_file_names=INCLUDE_PATTERN,
                                                     path_suffix=TFS_PATH_SUFFIX
                                                     )
    project_configuration = ProjectConfiguration(name='Test Project 4', id='test-project-004',
                                                 profile=ANALYSIS_PROFILE, connectors=[tfs_config])
    client.create_project(project_configuration=project_configuration)


def create_project_with_svn_connector():
    svn_config = SubversionSourceCodeConnectorConfiguration(account=ACCOUNT_NAME_SVN, repository_identifier='SVN',
                                                            included_file_names=INCLUDE_PATTERN)
    project_configuration = ProjectConfiguration(name='Test Project 5', id='test-project-005',
                                                 profile=ANALYSIS_PROFILE, connectors=[svn_config])
    client.create_project(project_configuration=project_configuration)


def test_project_api():
    show_projects()

    create_project_with_file_system_connector()
    show_projects()

    update_project_with_file_system_connector()
    show_projects()

    create_project_with_git_connector()
    show_projects()

    create_project_with_multiversion_file_system_connector()
    show_projects()

    create_project_with_tfs_connector()
    show_projects()

    create_project_with_svn_connector()
    show_projects()


with openapi_client.ApiClient(configuration) as api_client:
    client = openapi_client.ProjectApi(api_client)

    try:
        test_project_api()
    except ApiException as e:
        print('Exception when calling ProjectApi: %s\n' % e)
