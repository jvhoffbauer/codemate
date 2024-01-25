    @app.get("/test1")
    @app.get("/test2")
    async def test(var: Annotated[str, Query()] = "bar"):
        return {"foo": var}