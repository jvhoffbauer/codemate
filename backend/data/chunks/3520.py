def test_path_param_lt_gt_0():
    response = client.get("/path/param-lt-gt/0")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "greater_than",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be greater than 1",
                    "input": "0",
                    "ctx": {"gt": 1.0},
                    "url": match_pydantic_error_url("greater_than"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value is greater than 1",
                    "type": "value_error.number.not_gt",
                    "ctx": {"limit_value": 1},
                }
            ]
        }
    )