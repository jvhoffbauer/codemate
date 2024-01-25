async def prepare_database(models) -> AsyncGenerator[None, None]:
    async with db.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)
        yield
        await conn.run_sync(models.Base.metadata.drop_all)