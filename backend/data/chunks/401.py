def test_json_schema_flat_model_pydantic_v1():
    assert FlatModel.schema() == {
        "title": "FlatModel",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "type": "string", "format": "uuid"},
            "enum_field": {"$ref": "#/definitions/MyEnum1"},
        },
        "required": ["id", "enum_field"],
        "definitions": {
            "MyEnum1": {
                "title": "MyEnum1",
                "description": "An enumeration.",
                "enum": ["A", "B"],
                "type": "string",
            }
        },
    }