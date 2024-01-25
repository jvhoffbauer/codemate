def get_current_user(oauth_header: str = Security(oid)):
    user = User(username=oauth_header)
    return user