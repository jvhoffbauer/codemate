def get_current_user(oauth_header: str = Security(api_key)):
    user = User(username=oauth_header)
    return user