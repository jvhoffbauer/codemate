async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}