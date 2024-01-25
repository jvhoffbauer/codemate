@router4_override.get(
    "/default5",
)
async def path5_default_router4_override(level5: str):
    return level5