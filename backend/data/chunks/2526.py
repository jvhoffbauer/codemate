@app.get("/sync_sync")
def get_sync_sync(state: str = Depends(generator_state)):
    return state