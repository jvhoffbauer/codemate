@pytest.fixture(name="client")
def get_client():
    from docs_src.security.tutorial003_an_py39 import app

    client = TestClient(app)
    return client