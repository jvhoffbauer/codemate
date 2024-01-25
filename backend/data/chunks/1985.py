@router.get("/timed")
async def timed():
    return {"message": "It's the time of my life"}