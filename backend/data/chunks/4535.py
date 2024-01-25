def get_client():
    from docs_src.body_updates.tutorial001_py310 import app

    client = TestClient(app)
    return client