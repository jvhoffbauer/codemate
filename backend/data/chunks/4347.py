@pytest.fixture(name="client")
def get_client() -> TestClient:
    from docs_src.separate_openapi_schemas.tutorial001_py310 import app

    client = TestClient(app)
    return client