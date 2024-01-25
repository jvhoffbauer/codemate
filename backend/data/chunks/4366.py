@needs_py39
def test_invalid_price(client: TestClient):
    response = client.put("/items/5", json={"item": {"name": "Foo", "price": -3.0}})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "greater_than",
                    "loc": ["body", "item", "price"],
                    "msg": "Input should be greater than 0",
                    "input": -3.0,
                    "ctx": {"gt": 0.0},
                    "url": match_pydantic_error_url("greater_than"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "ctx": {"limit_value": 0},
                    "loc": ["body", "item", "price"],
                    "msg": "ensure this value is greater than 0",
                    "type": "value_error.number.not_gt",
                }
            ]
        }
    )