def get_client():
    from docs_src.request_files.tutorial001_02_py310 import app

    client = TestClient(app)
    return client