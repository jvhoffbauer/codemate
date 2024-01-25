def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)