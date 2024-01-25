async def context_b(state: dict = Depends(context_a)):
    state["context_b"] = "started b"
    try:
        yield state
    finally:
        state["context_b"] = f"finished b with a: {state['context_a']}"