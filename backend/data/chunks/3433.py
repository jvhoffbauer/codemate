    async def test(var: Annotated[str, Query()] = "bar"):
        return {"foo": var}