async def retrieve_user(id: int):
    user: ORMUser = await ORMUser.get(id)
    return User.from_orm(user)