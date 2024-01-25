async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons