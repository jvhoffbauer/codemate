def init() -> None:
    logger.info("Initializing service")
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e
    if (
        os.environ.get("RUN_MIGRATION")
        and os.environ["RUN_MIGRATION"].lower() == "false"
    ):
        logger.info("Skipping migrations")
    else:
        logger.info("Running migrations")
        run_alembic_migrations()
    logger.info("Initializing database entries")
    init_db(db)
    logger.info("Service finished initializing")