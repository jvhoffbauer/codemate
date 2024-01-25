async def get_context_b_raise(state: dict = Depends(context_b)):
    assert state["context_b"] == "started b"
    assert state["context_a"] == "started a"
    raise OtherDependencyError()