@pytest.fixture(name="client")
def get_client():
    from .app_pv1 import app

    client = TestClient(app)
    return client