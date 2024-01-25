    async def method_middleware(ctx: JsonRpcContext):
        ctx.http_response.set_cookie(key="method_middleware_enter", value="3")
        yield
        ctx.http_response.set_cookie(key="method_middleware_exit", value="4")