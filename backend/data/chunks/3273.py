@app.get("/", dependencies=[Depends(parent_dep)])
async def get_main():
    return {"msg": "Hello World"}