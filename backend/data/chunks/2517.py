@app.get("/context_b")
async def get_context_b(state: dict = Depends(context_b)):
    return state