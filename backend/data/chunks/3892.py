@pytest.fixture(name="client")
def get_client():
    from docs_src.extra_models.tutorial005_py39 import app

    client = TestClient(app)
    return client