async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session