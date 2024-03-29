@needs_pydanticv1
def test_create_read(app: FastAPI):
    with TestClient(app) as client:
        note = {"text": "Foo bar", "completed": False}
        response = client.post("/notes/", json=note)
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["text"] == note["text"]
        assert data["completed"] == note["completed"]
        assert "id" in data
        response = client.get("/notes/")
        assert response.status_code == 200, response.text
        assert data in response.json()