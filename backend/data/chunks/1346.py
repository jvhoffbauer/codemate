async def override_dependency(q: str | None = None):
    return {"q": q, "skip": 5, "limit": 10}