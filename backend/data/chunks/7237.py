@router.get("/", response_model=List[UserOut], dependencies=[Depends(on_superuser)])
async def read_users(
    offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
):
    """
    Retrieve users.
    """
    users = await crud_user.get_multi(session, offset=offset, limit=limit)
    return users