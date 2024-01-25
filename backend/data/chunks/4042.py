def get_client():
    from docs_src.body_multiple_params.tutorial003 import app

    client = TestClient(app)
    return client