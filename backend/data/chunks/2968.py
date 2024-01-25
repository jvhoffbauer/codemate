def test_header_repr_ellipsis():
    assert repr(Header(...)) == IsOneOf(
        "Header(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Header(Ellipsis)",
    )