async def update_user(
    user_id: int, user_in: UserUpdate, session: AsyncSession = Depends(get_session)
):
    user = await crud_user.get(session, id=user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    try:
        user = await crud_user.update(
            session,
            db_obj=user,
            obj_in={
                **user_in.dict(exclude={"password"}, exclude_none=True),
                "hashed_password": get_password_hash(user_in.password),
            },
        )
    except IntegrityError:
        raise HTTPException(
            status_code=409, detail="User with this username already exits"
        )
    return user