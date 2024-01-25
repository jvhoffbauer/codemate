                async def process_fn(
                    fn: Callable[[], Coroutine[Any, Any, Any]]
                ) -> None:
                    result = await fn()
                    results.append(result)  # noqa: B023