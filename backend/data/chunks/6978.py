@pytest.fixture
def ep(ep_path):
    _calls = defaultdict(list)

    ep_middleware_var = contextvars.ContextVar("ep_middleware")
    method_middleware_var = contextvars.ContextVar("method_middleware")

    @contextlib.asynccontextmanager
    async def ep_handle_exception(_ctx: jsonrpc.JsonRpcContext):
        try:
            yield
        except RuntimeError as exc:
            logging.exception(str(exc), exc_info=exc)
            raise _TestError(unique_marker2)

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

    @contextlib.asynccontextmanager
    async def method_middleware(ctx):
        nonlocal _calls
        method_middleware_var.set("method_middleware-value")
        _calls[ctx.raw_request.get("id")].append(
            (
                "method_middleware",
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
                    "method_middleware",
                    "exit",
                    ctx.raw_request,
                    ctx.raw_response,
                    sys.exc_info()[0],
                )
            )

    ep = jsonrpc.Entrypoint(
        ep_path,
        middlewares=[ep_handle_exception, ep_middleware],
    )

    @ep.method(middlewares=[method_middleware])
    def probe(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        return data

    @ep.method(middlewares=[method_middleware])
    def probe_error() -> str:
        raise RuntimeError(unique_marker)

    @ep.method(middlewares=[method_middleware])
    def probe_context_vars() -> Tuple[str, str]:
        return ep_middleware_var.get(), method_middleware_var.get()

    ep.calls = _calls

    return ep