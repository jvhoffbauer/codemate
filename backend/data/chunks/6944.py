    @ep.method()
    def probe(
        data: str = Body(..., examples=["123"]),
    ) -> str:
        return data