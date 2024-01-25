def get_client():
    from docs_src.body_updates.tutorial001 import app

    client = TestClient(app)
    return client