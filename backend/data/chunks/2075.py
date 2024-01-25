async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]