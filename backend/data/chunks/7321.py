def read_user_by_id(user: models.User = Depends(get_user)):
    """Get a specific user by id."""
    return user