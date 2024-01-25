def test_validator_is_cloned(client: TestClient):
    with pytest.raises(ResponseValidationError) as err:
        client.get("/model/modelX")
    assert err.value.errors() == [
        IsDict(
            {
                "type": "value_error",
                "loc": ("response", "name"),
                "msg": "Value error, name must end in A",
                "input": "modelX",
                "ctx": {"error": HasRepr("ValueError('name must end in A')")},
                "url": match_pydantic_error_url("value_error"),
            }
        )
        | IsDict(
            # TODO remove when deprecating Pydantic v1
            {
                "loc": ("response", "name"),
                "msg": "name must end in A",
                "type": "value_error",
            }
        )
    ]