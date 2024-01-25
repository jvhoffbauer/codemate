@router4_override.get(
    "/override5",
    tags=["path5a", "path5b"],
    responses={
        405: {"description": "Client error level 5"},
        505: {"description": "Server error level 5"},
    },
    deprecated=True,
    callbacks=callback_router5.routes,
    dependencies=[Depends(dep5)],
    response_class=ResponseLevel5,
)
async def path5_override_router4_override(level5: str):
    return level5