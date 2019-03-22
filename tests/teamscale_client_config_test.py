from teamscale_client.teamscale_client_config import TeamscaleClientConfig


def test_is_configured():
    """Tests that the client configuration reports correctly, if it is sufficiently configured."""
    global_config = TeamscaleClientConfig(url='http://example.com', username='doe', access_token='secret')
    _assert_config_is_sufficient(global_config, True, False)

    project_specific_config = TeamscaleClientConfig(url='http://example.com', username='doe', access_token='secret',
                                                    project='my-project')
    _assert_config_is_sufficient(project_specific_config, True, True)

    not_project_specific_config = TeamscaleClientConfig(url='http://example.com', username='doe', access_token='secret',
                                                    project='')
    _assert_config_is_sufficient(not_project_specific_config, True, False)

    incomplete_config = TeamscaleClientConfig(url=None, username='doe', access_token='secret')
    _assert_config_is_sufficient(incomplete_config, False, False)


def _assert_config_is_sufficient(config, sufficient_for_global_client, sufficient_for_project_specific_client):
    """Asserts the given sufficiencies of the provided configuration."""
    assert config.is_sufficient() == sufficient_for_global_client
    assert config.is_sufficient(require_project_id=True) == sufficient_for_project_specific_client
