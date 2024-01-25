def options_item(item_id: str):
    return JSONResponse(None, headers={"x-fastapi-item-id": item_id})