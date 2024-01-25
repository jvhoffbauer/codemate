def read_users(session: SessionDep, skip: int = 0, limit: int = 100) -> List[UserOut]:
    """
    Retrieve users.
    """
    statement = select(User).offset(skip).limit(limit)
    users = session.exec(statement).all()
    return users  # type: ignore