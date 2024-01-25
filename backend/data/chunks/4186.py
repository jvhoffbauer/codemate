def test_post_broken_body(client: TestClient):
    response = client.post(
        "/items/",
        headers={"content-type": "application/json"},
        content="{some broken json}",
    )
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "json_invalid",
                    "loc": ["body", 1],
                    "msg": "JSON decode error",
                    "input": {},
                    "ctx": {
                        "error": "Expecting property name enclosed in double quotes"
                    },
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", 1],
                    "msg": "Expecting property name enclosed in double quotes: line 1 column 2 (char 1)",
                    "type": "value_error.jsondecode",
                    "ctx": {
                        "msg": "Expecting property name enclosed in double quotes",
                        "doc": "{some broken json}",
                        "pos": 1,
                        "lineno": 1,
                        "colno": 2,
                    },
                }
            ]
        }
    )