@needs_pydanticv2
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
    # insert_assert(response.json())
    assert response.json() == {
        "detail": [
            {
                "type": "string_type",
                "loc": ["tags", 3],
                "msg": "Input should be a valid string",
                "input": {"sneaky": "object"},
                "url": match_pydantic_error_url("string_type"),
            }
        ]
    }