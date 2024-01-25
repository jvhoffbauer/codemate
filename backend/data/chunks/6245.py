async def async_session():
    async with async_db.session_maker() as session:
        yield session