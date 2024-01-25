def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client