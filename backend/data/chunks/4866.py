@pytest.fixture(name="client")
def get_client():
    from docs_src.security.tutorial005_py310 import app

    client = TestClient(app)
    return client