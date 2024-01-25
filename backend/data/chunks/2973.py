def test_cookie_repr_ellipsis():
    assert repr(Cookie(...)) == IsOneOf(
        "Cookie(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Cookie(Ellipsis)",
    )