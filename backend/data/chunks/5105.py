@router.get("/{username}", response_model=User)
def read_user(username: str, current_user: UserInDB = Depends(get_current_active_user)):
    """
    Get a specific user by username (email).
    """
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=username)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user