async def update_user(request: UserUpdateIn, id: int):
    user: ORMUser = await ORMUser.get(id)
    updated_fields: User = User.from_orm(request)
    await user.update(**updated_fields.dict(skip_defaults=True)).apply()
    return User.from_orm(user)