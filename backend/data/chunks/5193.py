async def task_io_bound():
    await asyncio.sleep(1)
    return "good result"