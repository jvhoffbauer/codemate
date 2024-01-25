@pytest.fixture
def ep_method_auth(ep):
    @ep.method()
    def probe(user: HTTPBasicCredentials = Depends(auth_user)) -> str:
        return user.username

    return ep