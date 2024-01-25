async def read_items(token: Optional[str] = Security(oauth2_scheme)):
    return {"token": token}