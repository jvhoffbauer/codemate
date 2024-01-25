        @app.get("/")
        async def get(item_id: Annotated[int, Query(default=1)]):
            pass  # pragma: nocover