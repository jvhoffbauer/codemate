def get_client():
    from docs_src.schema_extra_example.tutorial004_an_py39 import app

    client = TestClient(app)
    return client