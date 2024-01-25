@app.on_event("startup")
async def startup():
    await database.connect()