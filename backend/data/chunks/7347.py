def create_access_token(
    subject: str, expires_delta: timedelta | None = None, **kwargs
) -> str:
    if not isinstance(subject, str):
        raise ValueError("Subject must be a string")
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        **kwargs,
        "exp": expire.timestamp(),
        "sub": subject,
        "nbf": now,
        "iat": now,
    }
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_SIGNATURE_ALGORITHM
    )
    return encoded_jwt