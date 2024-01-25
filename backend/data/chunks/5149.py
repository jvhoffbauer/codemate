def get_password_hash(password: str):
    return pwd_context.hash(password)