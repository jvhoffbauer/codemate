@pytest.fixture(name="client")
def get_client():
    from docs_src.schema_extra_example.tutorial004_py310 import app

    client = TestClient(app)
    return client