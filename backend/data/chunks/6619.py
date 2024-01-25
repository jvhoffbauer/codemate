def generate_access_token_response(subject: str | int):
    """Generate tokens and return AccessTokenResponse"""
    access_token, expires_at, issued_at = create_jwt_token(
        subject, ACCESS_TOKEN_EXPIRE_SECS, refresh=False
    )
    refresh_token, refresh_expires_at, refresh_issued_at = create_jwt_token(
        subject, REFRESH_TOKEN_EXPIRE_SECS, refresh=True
    )
    return AccessTokenResponse(
        token_type="Bearer",
        access_token=access_token,
        expires_at=expires_at,
        issued_at=issued_at,
        refresh_token=refresh_token,
        refresh_token_expires_at=refresh_expires_at,
        refresh_token_issued_at=refresh_issued_at,
    )