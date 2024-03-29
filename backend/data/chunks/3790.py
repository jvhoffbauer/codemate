def test_items_plumbus_with_no_token(client: TestClient):
    response = client.get(
        "/items/plumbus", headers={"X-Token": "fake-super-secret-token"}
    )
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