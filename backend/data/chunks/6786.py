    @ep.method()
    def probe(
        data: List[str] = Body(..., examples=["111", "222"]),
        amount: int = Body(..., gt=5, examples=[10]),
    ) -> List[int]:
        del data, amount
        return [1, 2, 3]