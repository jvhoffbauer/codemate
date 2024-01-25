def authenticate(bucket: Bucket, *, username: str, password: str):
    user = get(bucket, username=username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user