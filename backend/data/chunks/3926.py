def get_client():
    from docs_src.body_nested_models.tutorial009 import app

    client = TestClient(app)
    return client