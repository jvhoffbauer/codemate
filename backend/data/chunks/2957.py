def test_param_repr_ellipsis():
    assert repr(Param(...)) == IsOneOf(
        "Param(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Param(Ellipsis)",
    )