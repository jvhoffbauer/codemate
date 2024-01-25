    async def __call__(self, value: str) -> AsyncGenerator[str, None]:
        yield value