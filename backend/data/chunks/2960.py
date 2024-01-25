def test_path_repr():
    assert repr(Path()) == IsOneOf(
        "Path(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Path(Ellipsis)",
    )
    assert repr(Path(...)) == IsOneOf(
        "Path(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Path(Ellipsis)",
    )