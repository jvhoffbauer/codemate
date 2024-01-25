@app.get("/main-depends/")
async def main_depends(commons: dict = Depends(common_parameters)):
    return {"in": "main-depends", "params": commons}