    @contextlib.asynccontextmanager
    async def mw_first(ctx: jsonrpc.JsonRpcContext):
        nonlocal _calls
        _calls[ctx.raw_request.get("id")].append(
            ("mw_first", "enter", ctx.raw_request, ctx.raw_response, sys.exc_info()[0])
        )
        try:
            yield
        finally:
            _calls[ctx.raw_response.get("id")].append(
                (
                    "mw_first",
                    "exit",
                    ctx.raw_request,
                    ctx.raw_response,
                    sys.exc_info()[0],
                )
            )