@pytest.fixture(name="client")
def get_client():
    from docs_src.extra_models.tutorial003_py310 import app

    client = TestClient(app)
    return client