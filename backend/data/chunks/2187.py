@app.post("/")
async def post(
    foo: Union[Foo, None] = None,
):
    return foo