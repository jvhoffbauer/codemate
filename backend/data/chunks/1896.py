async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}