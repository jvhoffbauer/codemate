@pytest.fixture(name="client")
def get_client():
    from docs_src.request_files.tutorial001_02_an_py310 import app

    client = TestClient(app)
    return client