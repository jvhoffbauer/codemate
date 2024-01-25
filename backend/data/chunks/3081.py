async def get_asynchronous_method_dependency(
    value: str = Depends(methods_dependency.asynchronous),
):
    return value