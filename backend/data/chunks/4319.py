def get_client():
    from docs_src.header_params.tutorial001_an_py310 import app

    client = TestClient(app)
    return client