@pytest.fixture(scope="module")
def client() -> Generator:
    """
    FastAPI对象
    :return:
    """
    app = create_app()
    with TestClient(app) as c:
        yield c