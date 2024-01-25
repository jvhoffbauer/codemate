@app.get("/check-class")
async def check_gzip_request(request: Request):
    return {"request_class": type(request).__name__}