@router.post("/open", response_model=User)
def create_user_open(
    *,
    username: str = Body(...),
    password: str = Body(...),
    email: EmailStr = Body(None),
    full_name: str = Body(None),
):
    """
    Create new user without the need to be logged in.
    """
    if not config.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user resistration is forbidden on this server",
        )
    bucket = get_default_bucket()
    user = crud.user.get(bucket, username=username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = UserCreate(
        username=username, password=password, email=email, full_name=full_name
    )
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    if config.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.username, password=user_in.password
        )
    return user