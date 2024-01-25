@app.get("/sync_async")
def get_sync_async(state: str = Depends(asyncgen_state)):
    return state