@pytest.fixture(name="client")
def get_client():
    from docs_src.header_params.tutorial003_py310 import app

    client = TestClient(app)
    return client