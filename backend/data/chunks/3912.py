def get_client():
    from docs_src.extra_models.tutorial004_py39 import app

    client = TestClient(app)
    return client