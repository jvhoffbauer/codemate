@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
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