async def startup(ctx):
    """
    Binds a connection set to the db object.
    """
    await db.set_bind(DATABASE_CONFIG.url)