@needs_pydanticv2
def test_model_field_default_required():
    # For coverage
    field_info = FieldInfo(annotation=str)
    field = ModelField(name="foo", field_info=field_info)
    assert field.default is Undefined