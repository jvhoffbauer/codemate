@app.get("/starlette-items/{item_id}")
async def read_starlette_item(item_id: str):
    if item_id not in items:
        raise StarletteHTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}