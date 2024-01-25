@needs_pydanticv1
def test_validator_is_cloned(client: TestClient):
    with pytest.raises(ResponseValidationError) as err:
        client.get("/model/modelX")
    assert err.value.errors() == [
        {
            "loc": ("response", "name"),
            "msg": "name must end in A",
            "type": "value_error",
        }
    ]