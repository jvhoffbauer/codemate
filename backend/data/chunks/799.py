@router.delete("/users/{id}", tags=["Users"], response_model=User)
async def delete_user(id: int):
    user: ORMUser = await ORMUser.get(id)
    return await user.delete()