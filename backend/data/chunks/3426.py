async def multiple(foo: Annotated[str, object(), Query(min_length=1)]):
    return {"foo": foo}