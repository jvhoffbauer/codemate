def test_override_with_sub__main_depends_q_foo():
    app.dependency_overrides[common_parameters] = overrider_dependency_with_sub
    response = client.get("/main-depends/?q=foo")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["query", "k"],
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
                    "loc": ["query", "k"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
    )
    app.dependency_overrides = {}