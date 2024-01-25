async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}