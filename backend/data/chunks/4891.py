def get_client(app: FastAPI):
    client = TestClient(app)
    return client