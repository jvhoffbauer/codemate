@pytest.fixture(autouse=True)
def app(set_env) -> TestClient:
    """Create App."""
    from titiler.application.main import app

    return TestClient(app)