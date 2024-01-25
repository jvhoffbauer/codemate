async def session(setup_db) -> AsyncSession:
    async with db.AsyncSession() as session:
        yield session