def get_current_user(oauth_header: "str" = Security(reusable_oauth2)):
    user = User(username=oauth_header)
    return user