def get_client():
    from docs_src.path_operation_configuration.tutorial005_py39 import app

    client = TestClient(app)
    return client