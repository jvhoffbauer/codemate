@app.get("/")
async def not_timed():
    return {"message": "Not timed"}