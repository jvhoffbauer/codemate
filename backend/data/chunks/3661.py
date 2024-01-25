@router.get(
    "/b",
    responses={
        502: {"description": "Error 2"},
        "4XX": {"description": "Error with range, upper"},
    },
)
async def b():
    return "b"