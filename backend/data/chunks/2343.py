def test_no_duplicates_invalid():
    response = client.post("/no-duplicates", json={"item": {"data": "myitem"}})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "item2"],
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
                    "loc": ["body", "item2"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )