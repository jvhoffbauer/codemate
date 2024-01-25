def get_client():
    from docs_src.body_multiple_params.tutorial001 import app

    client = TestClient(app)
    return client