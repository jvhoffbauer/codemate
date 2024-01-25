@app.get(
    "/override1",
    tags=["path1a", "path1b"],
    responses={
        401: {"description": "Client error level 1"},
        501: {"description": "Server error level 1"},
    },
    deprecated=True,
    callbacks=callback_router1.routes,
    dependencies=[Depends(dep1)],
    response_class=ResponseLevel1,
)
async def path1_override(level1: str):
    return level1