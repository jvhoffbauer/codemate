@app.get("/a", responses={"hello": {"description": "Not a valid additional response"}})
async def a():
    pass  # pragma: no cover