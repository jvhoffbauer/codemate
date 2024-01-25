@needs_pydanticv2
def test_post_broken_yaml(client: TestClient):
    yaml_data = """
        name: Deadpoolio
        tags:
        x - x-force
        x - x-men
        x - x-avengers
        """
    response = client.post("/items/", content=yaml_data)
    assert response.status_code == 422, response.text
    assert response.json() == {"detail": "Invalid YAML"}