def test_users_foo_with_no_token(client: TestClient):
    response = client.get("/users/foo")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["query", "token"],
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
                    "loc": ["query", "token"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )