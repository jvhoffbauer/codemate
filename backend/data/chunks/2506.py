async def get_async(state: str = Depends(asyncgen_state)):
    return state