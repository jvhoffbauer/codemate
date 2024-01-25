def get_client():
    from docs_src.body_fields.tutorial001_an import app

    client = TestClient(app)
    return client