    @ep.method(middlewares=[middleware])
    def probe() -> str:
        return "qwe"