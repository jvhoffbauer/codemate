@pytest.fixture(scope="session")
def health_client():
    return ApiClient(app)