async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user