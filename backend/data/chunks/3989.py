def get_client():
    from docs_src.extra_data_types.tutorial001_an_py39 import app

    client = TestClient(app)
    return client