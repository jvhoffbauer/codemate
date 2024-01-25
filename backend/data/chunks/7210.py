async def test_task(ctx, word: str):
    await asyncio.sleep(10)
    return f"test task return {word}"