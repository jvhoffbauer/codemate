    @contextlib.asynccontextmanager
    async def middleware(_ctx: JsonRpcContext):
        raise HTTPException(401)
        # noinspection PyUnreachableCode
        yield