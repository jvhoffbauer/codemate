def init() -> None:
    with Session(engine) as session:
        init_db(session)