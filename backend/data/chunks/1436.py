async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}