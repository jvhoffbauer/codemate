def test_strict_login_no_grant_type():
    response = client.post("/login", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "grant_type"],
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
                    "loc": ["body", "grant_type"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )