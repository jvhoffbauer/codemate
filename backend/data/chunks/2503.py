async def context_a(state: dict = Depends(get_state)):
    state["context_a"] = "started a"
    try:
        yield state
    finally:
        state["context_a"] = "finished a"