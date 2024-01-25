@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]