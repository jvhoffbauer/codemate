@app.post("/no-duplicates")
async def no_duplicates(item: Item, item2: Item = Depends(dependency)):
    return [item, item2]