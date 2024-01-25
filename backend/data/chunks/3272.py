async def parent_dep(result=Depends(response_status_setter)):
    return result