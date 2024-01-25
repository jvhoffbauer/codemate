async def overrider_dependency_simple(q: Optional[str] = None):
    return {"q": q, "skip": 5, "limit": 10}