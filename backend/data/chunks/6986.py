    @ep.method(middlewares=[method_middleware])
    def probe(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        return data