async def delete_user(id: int):
    user: ORMUser = await ORMUser.get(id)
    return await user.delete()