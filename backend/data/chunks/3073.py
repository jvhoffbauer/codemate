async def get_async_callable_dependency(
    value: str = Depends(async_callable_dependency),
):
    return value