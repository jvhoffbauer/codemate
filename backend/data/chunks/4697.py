def get_client():
    from docs_src.dependencies.tutorial006_an_py39 import app

    client = TestClient(app)
    return client