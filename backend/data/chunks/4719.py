def get_client():
    from docs_src.request_forms.tutorial001_an_py39 import app

    client = TestClient(app)
    return client