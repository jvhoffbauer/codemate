def test_path_param_gt_int_2():
    response = client.get("/path/param-gt-int/2")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "greater_than",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be greater than 3",
                    "input": "2",
                    "ctx": {"gt": 3},
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
                    "msg": "ensure this value is greater than 3",
                    "type": "value_error.number.not_gt",
                    "ctx": {"limit_value": 3},
                }
            ]
        }
    )