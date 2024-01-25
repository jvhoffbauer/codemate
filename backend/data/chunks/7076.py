def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.from_orm(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj