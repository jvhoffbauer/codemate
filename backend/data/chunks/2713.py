@app.trace("/items/{item_id}")
def trace_item(item_id: str):
    return JSONResponse(None, media_type="message/http")