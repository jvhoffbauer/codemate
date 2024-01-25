@app.get("/counter/")
async def get_counter(count: int = Depends(dep_counter)):
    return {"counter": count}