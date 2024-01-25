@app.get("/decorator-depends/", dependencies=[Depends(common_parameters)])
async def decorator_depends():
    return {"in": "decorator-depends"}