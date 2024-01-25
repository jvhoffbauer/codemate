def test_post_with_no_data(client: TestClient):
    response = client.post("/items/", json={})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "name"],
                    "msg": "Field required",
                    "input": {},
                    "url": match_pydantic_error_url("missing"),
                },
                {
                    "type": "missing",
                    "loc": ["body", "price"],
                    "msg": "Field required",
                    "input": {},
                    "url": match_pydantic_error_url("missing"),
                },
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "name"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
                {
                    "loc": ["body", "price"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]
        }
    )