def get_client():
    from docs_src.path_operation_advanced_configuration.tutorial007_pv1 import app

    client = TestClient(app)
    return client