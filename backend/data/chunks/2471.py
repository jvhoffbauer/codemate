@router2_default.get("/default3")
async def path3_default_router2_default(level3: str):
    return level3