@pytest.fixture(name="client")
def get_client():
    from docs_src.response_model.tutorial006_py310 import app

    client = TestClient(app)
    return client