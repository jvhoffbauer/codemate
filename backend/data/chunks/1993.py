@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]