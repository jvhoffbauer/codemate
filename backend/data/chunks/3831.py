@pytest.fixture(name="client")
def get_client():
    from docs_src.bigger_applications.app.main import app

    client = TestClient(app)
    return client