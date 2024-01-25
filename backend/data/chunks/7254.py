async def create_first_user(session: AsyncSession) -> None:
    email = settings.FIRST_USER_EMAIL
    password = get_password_hash(settings.FIRST_USER_PASSWORD.get_secret_value())
    result = await session.execute(select(User).where(User.email == email))
    user: Optional[User] = result.scalars().first()
    if user is None:
        session.add(User(email=email, hashed_password=password, is_superuser=True))
        await session.commit()