@pytest.fixture(name="client")
def get_client():
    from docs_src.additional_status_codes.tutorial001_py310 import app

    client = TestClient(app)
    return client