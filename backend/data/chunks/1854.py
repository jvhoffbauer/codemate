@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights