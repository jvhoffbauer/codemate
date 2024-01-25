@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c