async def super_dep(count: int = Depends(dep_counter)):
    return count