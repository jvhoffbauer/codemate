def get_client():
    from docs_src.body_nested_models.tutorial009_py39 import app

    client = TestClient(app)
    return client