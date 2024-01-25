@pytest.fixture
def raw_request(app_client, ep_path):
    def requester(body, path_postfix="", auth=None):
        resp = app_client.post(
            url=ep_path + path_postfix,
            content=body,
            auth=auth,
        )
        return resp

    return requester