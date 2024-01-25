def get_user_by_token(auth_token) -> User:
    return users[auth_token]