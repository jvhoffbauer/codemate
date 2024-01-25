@app.get("/http")
async def get_value_by_http(value: int = Depends(extract_value_from_http_connection)):
    return value