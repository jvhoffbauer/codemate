def get_client():
    from docs_src.dependencies.tutorial012_an_py39 import app

    client = TestClient(app)
    return client