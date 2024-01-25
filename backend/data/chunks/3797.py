def test_put_no_header(client: TestClient):
    response = client.put("/items/foo")
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["query", "token"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "missing",
                    "loc": ["header", "x-token"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["query", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["header", "x-token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )