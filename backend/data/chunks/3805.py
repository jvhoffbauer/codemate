def get_client():
    from docs_src.bigger_applications.app_an_py39.main import app

    client = TestClient(app)
    return client