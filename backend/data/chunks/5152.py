@pytest.fixture(scope="module")
def superuser_token_headers():
    return get_superuser_token_headers()