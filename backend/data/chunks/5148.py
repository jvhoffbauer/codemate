def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)