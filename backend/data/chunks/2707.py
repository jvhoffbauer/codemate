@app.head("/items/{item_id}")
def head_item(item_id: str):
    return JSONResponse(None, headers={"x-fastapi-item-id": item_id})