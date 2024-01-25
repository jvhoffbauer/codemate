def update_user_me(
    *,
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: UserInDB = Depends(get_current_active_user),
):
    """
    Update own user.
    """
    user_in = UserUpdate(**current_user.dict())
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    bucket = get_default_bucket()
    user = crud.user.update(bucket, username=current_user.username, user_in=user_in)
    return user