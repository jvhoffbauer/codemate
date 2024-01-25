    async def middleware(_ctx: JsonRpcContext):
        yield
        raise HTTPException(401)