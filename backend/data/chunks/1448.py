async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}