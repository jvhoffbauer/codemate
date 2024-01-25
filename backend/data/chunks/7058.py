def init() -> None:
    try:
        # Try to create session to check if DB is awake
        with Session(engine) as session:
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e