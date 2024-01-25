def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)