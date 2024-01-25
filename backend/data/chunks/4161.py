def test_post_invalid(client: TestClient):
    yaml_data = """
        name: Deadpoolio
        tags:
        - x-force
        - x-men
        - x-avengers
        - sneaky: object
        """
    response = client.post("/items/", content=yaml_data)
    assert response.status_code == 422, response.text
    assert response.json() == {
        "detail": [
            {"loc": ["tags", 3], "msg": "str type expected", "type": "type_error.str"}
        ]
    }