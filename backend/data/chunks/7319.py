def read_user_me(user: models.User = Depends(deps.get_current_active_user)):
    """Get current user."""
    return user