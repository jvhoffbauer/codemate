async def overrider_dependency_with_sub(msg: dict = Depends(overrider_sub_dependency)):
    return msg