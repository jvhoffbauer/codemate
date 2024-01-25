def test_jsonable_encoder_requiring_error():
    response = client.post("/items/", json=[{"name": "Foo", "age": -1.0}])
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "greater_than",
                    "loc": ["body", 0, "age"],
                    "msg": "Input should be greater than 0",
                    "input": -1.0,
                    "ctx": {"gt": 0},
                    "url": match_pydantic_error_url("greater_than"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "ctx": {"limit_value": 0.0},
                    "loc": ["body", 0, "age"],
                    "msg": "ensure this value is greater than 0",
                    "type": "value_error.number.not_gt",
                }
            ]
        }
    )