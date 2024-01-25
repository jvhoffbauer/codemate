@pytest.fixture(name="client")
def get_client():
    from docs_src.response_model.tutorial003_05_py310 import app

    client = TestClient(app)
    return client