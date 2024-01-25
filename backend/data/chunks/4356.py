@pytest.fixture(name="client")
def get_client():
    from docs_src.body_fields.tutorial001 import app

    client = TestClient(app)
    return client