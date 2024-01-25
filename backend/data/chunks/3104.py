@router.get("/router-depends/")
async def router_depends(commons: dict = Depends(common_parameters)):
    return {"in": "router-depends", "params": commons}