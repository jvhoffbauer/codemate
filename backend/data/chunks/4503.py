@app.get("/large")
async def large():
    return PlainTextResponse("x" * 4000, status_code=200)