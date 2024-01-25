def test_path_param_lt0_0():
    response = client.get("/path/param-lt0/0")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "less_than",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be less than 0",
                    "input": "0",
                    "ctx": {"lt": 0.0},
                    "url": match_pydantic_error_url("less_than"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value is less than 0",
                    "type": "value_error.number.not_lt",
                    "ctx": {"limit_value": 0},
                }
            ]
        }
    )