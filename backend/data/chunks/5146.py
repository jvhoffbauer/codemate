def config_couchbase(
    *, username, password, enterprise=False, host="couchbase", port="8091"
):
    allowed_username = get_allowed_username(username)
    assert (
        username == allowed_username
    ), f"Not a valid username: {username}, a valid one would be {allowed_username}"
    cluster_url = get_cluster_http_url(host=host, port=port)
    logger.info("before is_couchbase_ready")
    assert is_couchbase_ready(cluster_url)
    logger.info("after is_couchbase_ready")

    logger.info("before setup_couchbase_services")
    assert setup_couchbase_services(
        cluster_url=cluster_url,
        username=COUCHBASE_DEFAULT_USER,
        password=COUCHBASE_DEFAULT_PASSWORD,
    ) or setup_couchbase_services(
        cluster_url=cluster_url, username=username, password=password
    )
    logger.info("after setup_couchbase_services")

    logger.info("before setup_memory_quota")
    assert setup_memory_quota(
        cluster_url=cluster_url,
        username=COUCHBASE_DEFAULT_USER,
        password=COUCHBASE_DEFAULT_PASSWORD,
        memory_quota_mb=COUCHBASE_MEMORY_QUOTA_MB,
        fts_memory_quota_mb=COUCHBASE_FTS_MEMORY_QUOTA_MB,
        index_memory_quota_mb=COUCHBASE_INDEX_MEMORY_QUOTA_MB,
    ) or setup_memory_quota(
        cluster_url=cluster_url,
        username=username,
        password=password,
        memory_quota_mb=COUCHBASE_MEMORY_QUOTA_MB,
        fts_memory_quota_mb=COUCHBASE_FTS_MEMORY_QUOTA_MB,
        index_memory_quota_mb=COUCHBASE_INDEX_MEMORY_QUOTA_MB,
    )
    logger.info("after setup_memory_quota")

    if not enterprise:
        logger.info("before setup_index_storage")
        assert setup_index_storage(
            cluster_url=cluster_url,
            username=COUCHBASE_DEFAULT_USER,
            password=COUCHBASE_DEFAULT_PASSWORD,
        ) or setup_index_storage(
            cluster_url=cluster_url, username=username, password=password
        )
        logger.info("after setup_index_storage")

    logger.info("before ensure_couchbase_username_password")
    assert ensure_couchbase_username_password(
        cluster_url=cluster_url, username=username, password=password
    )
    logger.info("after ensure_couchbase_username_password")
    return True