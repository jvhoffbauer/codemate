def generate_password_reset_token(username):
    delta = timedelta(hours=config.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {
            "exp": exp,
            "nbf": now,
            "sub": password_reset_jwt_subject,
            "username": username,
        },
        config.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt