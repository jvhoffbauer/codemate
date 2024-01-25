@app.get("/default1")
async def path1_default(level1: str):
    return level1