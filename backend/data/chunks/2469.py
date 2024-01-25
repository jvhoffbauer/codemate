@router2_default.get(
    "/override3",
    tags=["path3a", "path3b"],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    deprecated=True,
    callbacks=callback_router3.routes,
    dependencies=[Depends(dep3)],
    response_class=ResponseLevel3,
)
async def path3_override_router2_default(level3: str):
    return level3