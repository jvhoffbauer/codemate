@router.get("/a", responses={501: {"description": "Error 1"}})
async def a():
    return "a"