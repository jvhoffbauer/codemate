def get_auth_token(
    auth_token: str = Header(..., alias="auth-token"),
) -> str:
    return auth_token