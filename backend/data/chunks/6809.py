@pytest.fixture
def app_client(app):
    return TestClient(app)