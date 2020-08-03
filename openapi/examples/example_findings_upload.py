from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import sys

import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models import ExternalAnalysisGroup
from openapi_client.models import ExternalFindingsDescription, ExternalFindingFileData, ExternalFindingData
from util.constants import Enablement, Assessment
from util.teamscale_utils import get_timestamp_parameter

from teamscale_client.constants import Enablement

TEAMSCALE_URL = 'http://localhost:8080'

USERNAME = 'user'
ACCESS_TOKEN = 'ide-access-token'
PROJECT_ID = 'test'

configuration = openapi_client.Configuration(
    host=TEAMSCALE_URL,
    username=USERNAME,
    password=ACCESS_TOKEN
)


def test_findings_api():
    # Add a new group that will contain findings
    findings_client.create_external_analysis_group(ExternalAnalysisGroup('Group 1', 'externals-.*'))

    # Make Teamscale aware of a new findings type, which maps to the previously
    # created group
    descriptions = [
        ExternalFindingsDescription('externals-1', None, 'A test finding description', Enablement.RED),
        ExternalFindingsDescription('externals-2', 'externals-2', 'Another finding description', Enablement.YELLOW)
    ]
    for finding_description in descriptions:
        findings_client.create_external_finding_description(finding_description)

    # A manual step to add the new groups to existing analysis profiles has to be done.
    if sys.version_info[0] == 2:
        input(
            'Please create the project or update the analysis profile used by the project to contain the new groups. '
            'Then Press ENTER to continue.')
    else:
        input(
            'Please create the project or update the analysis profile used by the project to contain the new groups. '
            'Then Press ENTER to continue.')

    # Update existing project to use new findings
    project_client.trigger_reanalysis(PROJECT_ID, only_findings_schema_update='true')

    # Upload findings to Teamscale
    findings = [
        ExternalFindingFileData([
            ExternalFindingData('externals-1', 'test2', Assessment.YELLOW, start_line=3,
                                finding_properties={'someStringProperty': 'severe', 'someNumericProperty': 42.0})
        ],
            'src/main/java/junit/extensions/ActiveTestSuite.java')
    ]
    external_analysis_client.upload_external_findings(PROJECT_ID, 'auto-create', findings,
                                                      t=get_timestamp_parameter(datetime.datetime.now()),
                                                      message='TestCommit',
                                                      partition='test-partition')


with openapi_client.ApiClient(configuration) as api_client:
    findings_client = openapi_client.FindingsApi(api_client)
    project_client = openapi_client.ProjectApi(api_client)
    external_analysis_client = openapi_client.ExternalAnalysisApi(api_client)

    try:
        test_findings_api()
    except ApiException as e:
        print('Exception when calling FindingsApi: %s\n' % e)
