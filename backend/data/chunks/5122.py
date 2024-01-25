def get_bucket(
    username: str,
    password: str,
    bucket_name: str,
    host="couchbase",
    port="8091",
    timeout: float = COUCHBASE_OPERATION_TIMEOUT_SECS,
    n1ql_timeout: float = COUCHBASE_N1QL_TIMEOUT_SECS,
):
    cluster = get_cluster(username, password, host=host, port=port)
    bucket: Bucket = cluster.open_bucket(bucket_name, lockmode=LOCKMODE_WAIT)
    bucket.timeout = timeout
    bucket.n1ql_timeout = n1ql_timeout
    return bucket