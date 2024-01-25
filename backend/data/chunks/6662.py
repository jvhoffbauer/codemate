def get_auth_user(
    # this will become the header-parameter of json-rpc method that uses this dependency
    auth_token: str = Header(
        None,
        alias="user-auth-token",
    ),
) -> User:
    if not auth_token:
        raise AuthError

    try:
        return get_user_by_token(auth_token)
    except KeyError:
        raise AuthError