def init():
    try:
        init_db()
    except Exception as e:
        logger.error(e)
        raise e