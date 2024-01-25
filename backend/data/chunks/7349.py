def verify_password_reset_token(token: str) -> str | None:
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.TOKEN_SIGNATURE_ALGORITHM]
        )
        return decoded_token["email"]
    except jwt.JWTError:
        return None