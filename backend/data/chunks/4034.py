def get_client():
    from docs_src.body_multiple_params.tutorial003_an_py310 import app

    client = TestClient(app)
    return client