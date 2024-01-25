async def shutdown(ctx):
    """
    Pops the bind on the db object.
    """
    await db.pop_bind().close()