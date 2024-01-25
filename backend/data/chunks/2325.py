@needs_pydanticv1
def test_union_scalar_list():
    # For coverage
    # TODO: there might not be a current valid code path that uses this, it would
    # potentially enable query parameters defined as both a scalar and a list
    # but that would require more refactors, also not sure it's really useful
    from fastapi._compat import is_pv1_scalar_field

    field_info = FieldInfo()
    field = ModelField(
        name="foo",
        field_info=field_info,
        type_=Union[str, List[int]],
        class_validators={},
        model_config=BaseConfig,
    )
    assert not is_pv1_scalar_field(field)