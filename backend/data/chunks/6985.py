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