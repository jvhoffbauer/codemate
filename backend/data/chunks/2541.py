async def get_sync_context_b_bg(
    tasks: BackgroundTasks, state: dict = Depends(context_b)
):
    async def bg(state: dict):
        state[
            "sync_bg"
        ] = f"sync_bg set - b: {state['context_b']} - a: {state['context_a']}"

    tasks.add_task(bg, state)
    return state