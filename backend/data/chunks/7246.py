async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_superuser),
    session: AsyncSession = Depends(get_session),
):
    user = await crud_user.get(session, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id == user_id:
        raise HTTPException(status_code=403, detail="User can't delete itself")
    await crud_user.delete(session, db_obj=user)