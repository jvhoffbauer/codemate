@app.get("/unrelated")
async def unrelated(foo: Annotated[str, object()]):
    return {"foo": foo}