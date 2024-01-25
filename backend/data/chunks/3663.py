@router.get(
    "/c",
    responses={
        "400": {"description": "Error with str"},
        "5xx": {"description": "Error with range, lower"},
        "default": {"description": "A default response"},
    },
)
async def c():
    return "c"