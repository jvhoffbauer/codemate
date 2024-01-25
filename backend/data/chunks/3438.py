def get_current_user(oauth_header: Optional[str] = Security(oid)):
    if oauth_header is None:
        return None
    user = User(username=oauth_header)
    return user