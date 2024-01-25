@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons