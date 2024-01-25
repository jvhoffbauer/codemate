@needs_pydanticv2
def test_post(client: TestClient):
    yaml_data = """
        name: Deadpoolio
        tags:
        - x-force
        - x-men
        - x-avengers
        """
    response = client.post("/items/", content=yaml_data)
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "Deadpoolio",
        "tags": ["x-force", "x-men", "x-avengers"],
    }