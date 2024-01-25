def ep(ep_path):
    _calls = defaultdict(list)

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

    @contextlib.asynccontextmanager
    async def mw_last(ctx: jsonrpc.JsonRpcContext):
        nonlocal _calls
        _calls[ctx.raw_request.get("id")].append(
            ("mw_last", "enter", ctx.raw_request, ctx.raw_response, sys.exc_info()[0])
        )
        try:
            yield
        finally:
            _calls[ctx.raw_response.get("id")].append(
                (
                    "mw_last",
                    "exit",
                    ctx.raw_request,
                    ctx.raw_response,
                    sys.exc_info()[0],
                )
            )

    ep = jsonrpc.Entrypoint(
        ep_path,
        middlewares=[mw_first, mw_exception_enter, mw_last],
    )

    @ep.method()
    def probe(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        return data

    ep.calls = _calls

    return ep