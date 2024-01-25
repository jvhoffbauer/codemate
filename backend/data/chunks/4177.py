def client():
    from docs_src.body.tutorial001 import app

    client = TestClient(app)
    return client