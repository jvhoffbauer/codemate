async def staff(session: AsyncSession):
    adal = AsyncDal(session)
    ins = adal.add(
        Staff,
        name="admin",
    )
    await adal.commit()
    return ins