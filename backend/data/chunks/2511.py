@app.get("/sync_raise")
async def get_sync_raise(state: str = Depends(generator_state_try)):
    assert state == "generator raise started"
    raise SyncDependencyError()