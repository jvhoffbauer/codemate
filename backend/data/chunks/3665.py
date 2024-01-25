@router.get(
    "/d",
    responses={
        "400": {"description": "Error with str"},
        "5XX": {"model": ResponseModel},
        "default": {"model": ResponseModel},
    },
)
async def d():
    return "d"