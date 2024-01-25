@app.post("/with-duplicates")
async def with_duplicates(item: Item, item2: Item = Depends(duplicate_dependency)):
    return [item, item2]