def get_current_user(token: str = Security(reusable_oauth2)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=token_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user