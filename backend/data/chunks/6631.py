async def default_user(test_db_setup_sessionmaker) -> User:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.email == default_user_email)
        )
        user = result.scalars().first()
        if user is None:
            new_user = User(
                email=default_user_email,
                hashed_password=default_user_password_hash,
            )
            new_user.id = default_user_id
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
        return user