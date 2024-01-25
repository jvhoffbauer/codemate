def user_client(user: User):
    return ApiClient(app, user)