@pytest.fixture(name="client")
def get_client():
    from docs_src.request_forms.tutorial001 import app

    client = TestClient(app)
    return client