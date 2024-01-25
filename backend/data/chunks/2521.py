@app.get("/context_b_bg")
async def get_context_b_bg(tasks: BackgroundTasks, state: dict = Depends(context_b)):
    async def bg(state: dict):
        state["bg"] = f"bg set - b: {state['context_b']} - a: {state['context_a']}"

    tasks.add_task(bg, state)
    return state