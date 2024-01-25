@pytest.fixture(name="client")
def get_client():
    from docs_src.query_params.tutorial006_py310 import app

    c = TestClient(app)
    return c