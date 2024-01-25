@router.post("/", response_model=UserOut, dependencies=[Depends(on_superuser)])
async def create_user(
    user_in: UserCreate, session: AsyncSession = Depends(get_session)
):
    """
    Create new user.
    """
    user = await crud_user.get(session, email=user_in.email)
    if user is not None:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system",
        )
    obj_in = UserInDB(
        **user_in.dict(), hashed_password=get_password_hash(user_in.password)
    )
    return await crud_user.create(session, obj_in)