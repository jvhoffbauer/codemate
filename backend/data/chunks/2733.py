@app.get("/items/")
async def read_items():
    return {"id": "foo"}