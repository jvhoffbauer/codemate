def get_client():
    from docs_src.query_params_str_validations.tutorial011_an_py39 import app

    client = TestClient(app)
    return client