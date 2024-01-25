    @contextlib.asynccontextmanager
    async def ep_middleware(ctx: JsonRpcContext):
        ctx.http_response.set_cookie(key="ep_middleware_enter", value="1")
        yield
        ctx.http_response.set_cookie(key="ep_middleware_exit", value="2")