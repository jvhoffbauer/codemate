def get_client():
    from docs_src.security.tutorial003_py310 import app

    client = TestClient(app)
    return client