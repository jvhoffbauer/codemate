def get_client():
    from docs_src.security.tutorial005_an_py39 import app

    client = TestClient(app)
    return client