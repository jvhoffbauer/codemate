def read_user_me(current_user: UserInDB = Depends(get_current_active_user)):
    """
    Get current user.
    """
    return current_user