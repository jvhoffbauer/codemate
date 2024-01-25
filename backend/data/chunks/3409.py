        @app.get("/items/{item_id}/")
        async def get_item(item_id: Annotated[int, Path(default=1)]):
            pass  # pragma: nocover