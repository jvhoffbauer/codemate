@needs_py310
def test_read_items(client: TestClient) -> None:
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {
            "name": "Portal Gun",
            "description": "Device to travel through the multi-rick-verse",
        },
        {"name": "Plumbus", "description": None},
    ]