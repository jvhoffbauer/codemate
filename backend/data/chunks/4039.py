@pytest.fixture(name="client")
def get_client():
    from docs_src.body_multiple_params.tutorial001_an import app

    client = TestClient(app)
    return client