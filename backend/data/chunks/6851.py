    async def get_shared_counter(
        shared: str = Header("shared"),
    ) -> str:
        nonlocal _shared_counter
        _shared_counter += 1
        yield f"{shared}-{_shared_counter}"