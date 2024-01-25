@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item