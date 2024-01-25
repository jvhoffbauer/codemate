def get_client() -> TestClient:
    from docs_src.separate_openapi_schemas.tutorial002_py39 import app

    client = TestClient(app)
    return client