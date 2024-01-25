async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user