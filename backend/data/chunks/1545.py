@app.get("/items/", response_model=list[Item])
async def read_items():
    return items