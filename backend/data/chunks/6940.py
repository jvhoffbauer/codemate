    @contextlib.asynccontextmanager
    async def mw_exception_enter(ctx: jsonrpc.JsonRpcContext):
        nonlocal _calls
        _calls[ctx.raw_request.get("id")].append(
            (
                "mw_exception_enter",
                "enter",
                ctx.raw_request,
                ctx.raw_response,
                sys.exc_info()[0],
            )
        )
        raise RuntimeError(unique_marker)
        # noinspection PyUnreachableCode
        try:
            yield
        finally:
            _calls[ctx.raw_response.get("id")].append(
                (
                    "mw_exception_enter",
                    "exit",
                    ctx.raw_request,
                    ctx.raw_response,
                    sys.exc_info()[0],
                )
            )