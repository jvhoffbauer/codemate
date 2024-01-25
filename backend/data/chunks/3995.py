def get_client():
    from docs_src.extra_data_types.tutorial001_py310 import app

    client = TestClient(app)
    return client