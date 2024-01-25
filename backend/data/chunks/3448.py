async def hidden_path(hidden_path: str = Path(include_in_schema=False)):
    return {"hidden_path": hidden_path}