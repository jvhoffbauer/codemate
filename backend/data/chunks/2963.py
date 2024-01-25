def test_query_repr_ellipsis():
    assert repr(Query(...)) == IsOneOf(
        "Query(PydanticUndefined)",
        # TODO: remove when deprecating Pydantic v1
        "Query(Ellipsis)",
    )