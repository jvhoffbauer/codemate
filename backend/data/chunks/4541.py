def get_client():
    from docs_src.body_updates.tutorial001_py39 import app

    client = TestClient(app)
    return client