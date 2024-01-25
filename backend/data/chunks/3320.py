@app.get("/b", responses={204: {"description": "No Content"}})
async def b():
    pass  # pragma: no cover