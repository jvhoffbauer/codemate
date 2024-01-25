    @ep.method(middlewares=[method_middleware])
    def probe_context_vars() -> Tuple[str, str]:
        return ep_middleware_var.get(), method_middleware_var.get()