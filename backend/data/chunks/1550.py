async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved