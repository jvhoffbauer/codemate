@pytest.fixture(name="client")
def get_client():
    from docs_src.security.tutorial006_an import app

    client = TestClient(app)
    return client