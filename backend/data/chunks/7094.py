def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> list[ItemOut]:
    """
    Retrieve items.
    """

    if current_user.is_superuser:
        statement = select(Item).offset(skip).limit(limit)
        return session.exec(statement).all()  # type: ignore
    else:
        statement = (
            select(Item)
            .where(Item.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        return session.exec(statement).all()  # type: ignore