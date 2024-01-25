async def shutdown():
    await database.disconnect()