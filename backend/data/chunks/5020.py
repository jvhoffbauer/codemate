def init():
    try:
        # Check Couchbase is awake
        bucket = get_default_bucket()
        logger.info(
            f"Database bucket connection established with bucket object: {bucket}"
        )
    except Exception as e:
        logger.error(e)
        raise e