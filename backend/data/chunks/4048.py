def get_client():
    from docs_src.query_params_str_validations.tutorial014_an_py39 import app

    client = TestClient(app)
    return client