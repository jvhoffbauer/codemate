def recover_password(username: str):
    """
    Password Recovery.
    """
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=username)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(username=username)
    send_reset_password_email(
        email_to=user.email, username=username, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}