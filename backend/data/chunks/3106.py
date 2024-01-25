@router.get("/router-decorator-depends/", dependencies=[Depends(common_parameters)])
async def router_decorator_depends():
    return {"in": "router-decorator-depends"}