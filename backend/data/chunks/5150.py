@pytest.fixture(scope="module")
def server_api():
    return get_server_api()