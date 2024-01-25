@pytest.fixture
def ep(ep_path):
    return jsonrpc.Entrypoint(ep_path)