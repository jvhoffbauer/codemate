def test_strict_login_incorrect_grant_type():
    response = client.post(
        "/login",
        data={"username": "johndoe", "password": "secret", "grant_type": "incorrect"},
    )
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "string_pattern_mismatch",
                    "loc": ["body", "grant_type"],
                    "msg": "String should match pattern 'password'",
                    "input": "incorrect",
                    "ctx": {"pattern": "password"},
                    "url": match_pydantic_error_url("string_pattern_mismatch"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "grant_type"],
                    "msg": 'string does not match regex "password"',
                    "type": "value_error.str.regex",
                    "ctx": {"pattern": "password"},
                }
            ]
        }
    )