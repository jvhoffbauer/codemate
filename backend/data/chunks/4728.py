def get_client() -> TestClient:
    from docs_src.conditional_openapi import tutorial001

    importlib.reload(tutorial001)

    client = TestClient(tutorial001.app)
    return client