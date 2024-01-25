@router.put("/{username}", response_model=User)
def update_user(
    *,
    username: str,
    user_in: UserUpdate,
    current_user: UserInDB = Depends(get_current_active_superuser),
):
    """
    Update a user.
    """
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=username)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(bucket, username=username, user_in=user_in)
    return user