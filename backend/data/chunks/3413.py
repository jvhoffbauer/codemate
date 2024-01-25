def test_no_multiple_annotations():
    async def dep():
        pass  # pragma: nocover

    with pytest.raises(
        AssertionError,
        match="Cannot specify multiple `Annotated` FastAPI arguments for 'foo'",
    ):

        @app.get("/")
        async def get(foo: Annotated[int, Query(min_length=1), Query()]):
            pass  # pragma: nocover

    with pytest.raises(
        AssertionError,
        match=(
            "Cannot specify `Depends` in `Annotated` and default value"
            " together for 'foo'"
        ),
    ):

        @app.get("/")
        async def get2(foo: Annotated[int, Depends(dep)] = Depends(dep)):
            pass  # pragma: nocover

    with pytest.raises(
        AssertionError,
        match=(
            "Cannot specify a FastAPI annotation in `Annotated` and `Depends` as a"
            " default value together for 'foo'"
        ),
    ):

        @app.get("/")
        async def get3(foo: Annotated[int, Query(min_length=1)] = Depends(dep)):
            pass  # pragma: nocover