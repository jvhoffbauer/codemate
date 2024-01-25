def test_put_incorrect_body_multiple():
    response = client.post("/items/", json=[{"age": "five"}, {"age": "six"}])
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", 0, "name"],
                    "msg": "Field required",
                    "input": {"age": "five"},
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "decimal_parsing",
                    "loc": ["body", 0, "age"],
                    "msg": "Input should be a valid decimal",
                    "input": "five",
                    "url": match_pydantic_error_url("decimal_parsing"),
                },
                {
                    "type": "missing",
                    "loc": ["body", 1, "name"],
                    "msg": "Field required",
                    "input": {"age": "six"},
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "decimal_parsing",
                    "loc": ["body", 1, "age"],
                    "msg": "Input should be a valid decimal",
                    "input": "six",
                    "url": match_pydantic_error_url("decimal_parsing"),
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", 0, "name"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", 0, "age"],
                    "msg": "value is not a valid decimal",
                    "type": "type_error.decimal",
                },
                {
                    "loc": ["body", 1, "name"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", 1, "age"],
                    "msg": "value is not a valid decimal",
                    "type": "type_error.decimal",
                },
            ]
        }
    )