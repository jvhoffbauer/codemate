def get_client():
    from docs_src.request_forms.tutorial001_an import app

    client = TestClient(app)
    return client