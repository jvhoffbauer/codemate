@app.get("/sync_context_b")
def get_sync_context_b(state: dict = Depends(context_b)):
    return state