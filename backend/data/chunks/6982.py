    @contextlib.asynccontextmanager
    async def ep_middleware(ctx: jsonrpc.JsonRpcContext):
        nonlocal _calls
        ep_middleware_var.set("ep_middleware-value")
        _calls[ctx.raw_request.get("id")].append(
            (
                "ep_middleware",
                "enter",
                ctx.raw_request,
                ctx.raw_response,
                sys.exc_info()[0],
            )
        )
        try:
            yield
        finally:
            _calls[ctx.raw_response.get("id")].append(
                (
                    "ep_middleware",
                    "exit",
                    ctx.raw_request,
                    ctx.raw_response,
                    sys.exc_info()[0],
                )
            )