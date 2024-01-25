        @app.get("/")
        async def get(foo: Annotated[int, Query(min_length=1), Query()]):
            pass  # pragma: nocover