def auth_user(
    credentials: HTTPBasicCredentials = Depends(security),
) -> HTTPBasicCredentials:
    if (credentials.username, credentials.password) != ("user", "password"):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials