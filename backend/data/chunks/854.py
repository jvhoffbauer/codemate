async def get_user_by_email(email: str) -> dict[str, Any] | None:
    select_query = select(auth_user).where(auth_user.c.email == email)

    return await fetch_one(select_query)