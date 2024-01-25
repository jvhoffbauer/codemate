def test_json_schema_inherit_model_pydantic_v1():
    assert InheritModel.schema() == {
        "title": "InheritModel",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "type": "string", "format": "uuid"},
            "enum_field": {"$ref": "#/definitions/MyEnum2"},
        },
        "required": ["id", "enum_field"],
        "definitions": {
            "MyEnum2": {
                "title": "MyEnum2",
                "description": "An enumeration.",
                "enum": ["C", "D"],
                "type": "string",
            }
        },
    }