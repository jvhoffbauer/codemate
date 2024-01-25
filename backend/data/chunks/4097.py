@pytest.fixture(name="client")
def get_client():
    from docs_src.query_params_str_validations.tutorial010_an import app

    client = TestClient(app)
    return client