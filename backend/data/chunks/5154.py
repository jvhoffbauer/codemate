@pytest.fixture(scope="module")
def normal_user_token_headers():
    return authentication_token_from_email(config.EMAIL_TEST_USER)