@app.post("/items/")
async def create_item(item: Item):
    return item