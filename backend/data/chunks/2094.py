@router.get("/")
async def read_items():
    return fake_items_db