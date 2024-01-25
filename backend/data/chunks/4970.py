def get_client():
    from docs_src.request_files.tutorial001_03_an_py39 import app

    client = TestClient(app)
    return client