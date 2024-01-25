    async def asynchronous_gen(self, value: str) -> AsyncGenerator[str, None]:
        yield value