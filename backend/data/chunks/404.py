@needs_pydanticv2
def test_json_schema_flat_model_pydantic_v2():
    assert FlatModel.model_json_schema() == {
        "title": "FlatModel",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "type": "string", "format": "uuid"},
            "enum_field": {"$ref": "#/$defs/MyEnum1"},
        },
        "required": ["id", "enum_field"],
        "$defs": {
            "MyEnum1": {"enum": ["A", "B"], "title": "MyEnum1", "type": "string"}
        },
    }