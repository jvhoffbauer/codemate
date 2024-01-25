@pytest.fixture(name="client")
def get_client():
    from docs_src.path_operation_advanced_configuration.tutorial007 import app

    client = TestClient(app)
    return client