def get_password_hash(password):
    return pwd_context.hash(password)