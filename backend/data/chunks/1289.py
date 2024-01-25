@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item