def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_superuser),
):
    """
    Retrieve users.
    """
    bucket = get_default_bucket()
    users = crud.user.get_multi(bucket, skip=skip, limit=limit)
    return users