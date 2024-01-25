def test_multi_query_incorrect():
    response = client.get("/items/?q=five&q=six")
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "int_parsing",
                    "loc": ["query", "q", 0],
                    "msg": "Input should be a valid integer, unable to parse string as an integer",
                    "input": "five",
                    "url": match_pydantic_error_url("int_parsing"),
                },
                {
                    "type": "int_parsing",
                    "loc": ["query", "q", 1],
                    "msg": "Input should be a valid integer, unable to parse string as an integer",
                    "input": "six",
                    "url": match_pydantic_error_url("int_parsing"),
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["query", "q", 0],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                },
                {
                    "loc": ["query", "q", 1],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                },
            ]
        }
    )