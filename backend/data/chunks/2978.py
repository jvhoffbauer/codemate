def test_body_repr_ellipsis():
    assert repr(Body(...)) == IsOneOf(
        "Body(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Body(Ellipsis)",
    )