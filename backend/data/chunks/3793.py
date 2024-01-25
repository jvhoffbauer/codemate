def test_items_with_missing_x_token_header(client: TestClient):
    response = client.get("/items?token=jessica")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["header", "x-token"],
                    "msg": "Field required",
                    "input": None,
                    "url": match_pydantic_error_url("missing"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["header", "x-token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )