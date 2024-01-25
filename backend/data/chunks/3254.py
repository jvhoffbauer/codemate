@app.get("/http-exception")
def route_with_http_exception():
    raise HTTPException(status_code=400)