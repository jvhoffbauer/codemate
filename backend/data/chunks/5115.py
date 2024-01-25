@router.post("/reset-password/", response_model=Msg)
def reset_password(token: str = Body(...), new_password: str = Body(...)):
    """
    Reset password.
    """
    username = verify_password_reset_token(token)
    if not username:
        raise HTTPException(status_code=400, detail="Invalid token")
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=username)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    user_in = UserUpdate(name=username, password=new_password)
    user = crud.user.update(bucket, username=username, user_in=user_in)
    return {"msg": "Password updated successfully"}