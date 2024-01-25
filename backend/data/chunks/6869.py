    @ep.method()
    def probe(
        data: List[str] = Body(..., examples=["111", "222"]),
    ) -> List[int]:
        del data
        return [1, 2, 3]