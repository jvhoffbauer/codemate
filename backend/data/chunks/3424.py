async def required(foo: Annotated[str, Query(min_length=1)]):
    return {"foo": foo}