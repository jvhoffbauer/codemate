@pytest.fixture(name="client")
def get_client():
    from docs_src.schema_extra_example.tutorial005_an import app

    client = TestClient(app)
    return client