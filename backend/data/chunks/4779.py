@pytest.fixture(name="client")
def get_client():
    from docs_src.security.tutorial001_an_py39 import app

    client = TestClient(app)
    return client