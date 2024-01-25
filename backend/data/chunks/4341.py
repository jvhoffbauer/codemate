def get_client() -> TestClient:
    from docs_src.separate_openapi_schemas.tutorial002 import app

    client = TestClient(app)
    return client