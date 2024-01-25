def test_get_enums_invalid():
    response = client.get("/models/foo")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "enum",
                    "loc": ["path", "model_name"],
                    "msg": "Input should be 'alexnet', 'resnet' or 'lenet'",
                    "input": "foo",
                    "ctx": {"expected": "'alexnet', 'resnet' or 'lenet'"},
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "ctx": {"enum_values": ["alexnet", "resnet", "lenet"]},
                    "loc": ["path", "model_name"],
                    "msg": "value is not a valid enumeration member; permitted: 'alexnet', 'resnet', 'lenet'",
                    "type": "type_error.enum",
                }
            ]
        }
    )