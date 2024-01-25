@app.get("/items/", response_model=List[Item])
async def read_items():
    return items