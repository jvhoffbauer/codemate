@router2_override.get("/default3")
async def path3_default_router2_override(level3: str):
    return level3