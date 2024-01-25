def init():
    try:
        # Check Couchbase is awake
        bucket = get_default_bucket()
        logger.info(
            f"Database bucket connection established with bucket object: {bucket}"
        )

        # Wait for API to be awake, run one simple tests to authenticate
        test_get_access_token()
    except Exception as e:
        logger.error(e)
        raise e