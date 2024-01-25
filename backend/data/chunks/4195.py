def client():
    from docs_src.body.tutorial001_py310 import app

    client = TestClient(app)
    return client