def get_client():
    from docs_src.schema_extra_example.tutorial005 import app

    client = TestClient(app)
    return client