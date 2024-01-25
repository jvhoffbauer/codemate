@pytest.fixture(name="client")
def get_client():
    from docs_src.dependencies.tutorial004_py310 import app

    client = TestClient(app)
    return client