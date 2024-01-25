@app.get("/sync")
async def get_sync(state: str = Depends(generator_state)):
    return state