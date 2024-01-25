async def _setup_async_db() -> AsyncDatabase:
    yield async_db
    await async_db.async_close()  # Free connection pool resources