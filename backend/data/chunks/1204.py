async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user