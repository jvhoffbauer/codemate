    @ep.method(middlewares=[method_middleware])
    def probe_error() -> str:
        raise RuntimeError(unique_marker)