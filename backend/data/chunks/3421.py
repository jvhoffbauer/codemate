@app.get("/default")
async def default(foo: Annotated[str, Query()] = "foo"):
    return {"foo": foo}