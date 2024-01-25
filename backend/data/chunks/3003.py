def test_query_params_str_validations_item_query_nonregexquery():
    client = get_client()
    response = client.get("/items/", params={"q": "nonregexquery"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "string_pattern_mismatch",
                    "loc": ["query", "q"],
                    "msg": "String should match pattern '^fixedquery$'",
                    "input": "nonregexquery",
                    "ctx": {"pattern": "^fixedquery$"},
                    "url": match_pydantic_error_url("string_pattern_mismatch"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "ctx": {"pattern": "^fixedquery$"},
                    "loc": ["query", "q"],
                    "msg": 'string does not match regex "^fixedquery$"',
                    "type": "value_error.str.regex",
                }
            ]
        }
    )