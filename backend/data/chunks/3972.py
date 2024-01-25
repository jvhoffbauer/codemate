def get_client():
    from docs_src.response_model.tutorial003_01_py310 import app

    client = TestClient(app)
    return client