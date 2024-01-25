def test_events(app: FastAPI):
    with TestClient(app) as client:
        response = client.get("/items/")
        assert response.status_code == 200, response.text
        assert response.json() == [{"name": "Foo"}]
    with open("log.txt") as log:
        assert "Application shutdown" in log.read()