@app.get("/sync_context_b_raise")
def get_sync_context_b_raise(state: dict = Depends(context_b)):
    assert state["context_b"] == "started b"
    assert state["context_a"] == "started a"
    raise OtherDependencyError()