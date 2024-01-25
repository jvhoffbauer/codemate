@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]