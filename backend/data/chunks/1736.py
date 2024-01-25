@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons