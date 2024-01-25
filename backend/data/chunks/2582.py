@app.get("/b", responses={500: {"description": "Error", "model": Error}})
async def b():
    pass  # pragma: no cover