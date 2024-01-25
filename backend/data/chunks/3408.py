def test_no_annotated_defaults():
    with pytest.raises(
        AssertionError, match="Path parameters cannot have a default value"
    ):

        @app.get("/items/{item_id}/")
        async def get_item(item_id: Annotated[int, Path(default=1)]):
            pass  # pragma: nocover

    with pytest.raises(
        AssertionError,
        match=(
            "`Query` default value cannot be set in `Annotated` for 'item_id'. Set the"
            " default value with `=` instead."
        ),
    ):

        @app.get("/")
        async def get(item_id: Annotated[int, Query(default=1)]):
            pass  # pragma: nocover