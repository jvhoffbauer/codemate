def get_client():
    from docs_src.query_params.tutorial006 import app

    c = TestClient(app)
    return c