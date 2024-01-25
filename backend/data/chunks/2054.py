@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()