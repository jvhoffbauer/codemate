        async def get3(foo: Annotated[int, Query(min_length=1)] = Depends(dep)):
            pass  # pragma: nocover