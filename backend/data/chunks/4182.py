def test_post_with_only_name(client: TestClient):
    response = client.post("/items/", json={"name": "Foo"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "price"],
                    "msg": "Field required",
                    "input": {"name": "Foo"},
                    "url": match_pydantic_error_url("missing"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "price"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )