@app.get("/sync_sync_raise_other")
def get_sync_sync_raise_other(state: str = Depends(generator_state_try)):
    assert state == "generator raise started"
    raise OtherDependencyError()