def get_client():
    from docs_src.schema_extra_example.tutorial001_pv1 import app

    client = TestClient(app)
    return client