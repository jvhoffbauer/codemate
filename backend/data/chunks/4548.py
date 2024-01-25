def test_events(app: FastAPI):
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200, response.text
        assert response.json() == {"name": "Fighters"}