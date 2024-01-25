    async def get_common_counter(
        common: str = Body(...),
    ) -> str:
        nonlocal _common_counter
        _common_counter += 1
        yield f"{common}-{_common_counter}"