def client() -> Generator:
    with TestClient(app) as client:
        yield client