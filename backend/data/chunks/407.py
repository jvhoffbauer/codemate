def test_json_schema_inherit_model_pydantic_v2():
    assert InheritModel.model_json_schema() == {
        "title": "InheritModel",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "type": "string", "format": "uuid"},
            "enum_field": {"$ref": "#/$defs/MyEnum2"},
        },
        "required": ["id", "enum_field"],
        "$defs": {
            "MyEnum2": {"enum": ["C", "D"], "title": "MyEnum2", "type": "string"}
        },
    }