@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item