@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]