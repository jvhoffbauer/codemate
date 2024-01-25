@app.get("/sync_raise_other")
async def get_sync_raise_other(state: str = Depends(generator_state_try)):
    assert state == "generator raise started"
    raise OtherDependencyError()