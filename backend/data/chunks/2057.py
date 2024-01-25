async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)