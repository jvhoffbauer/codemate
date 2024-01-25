def ensure_create_bucket(
    *,
    cluster_url,
    username,
    password,
    bucket_name,
    ram_quota_mb=100,
    bucket_type="couchbase",
):
    if is_bucket_created(
        cluster_url=cluster_url,
        username=username,
        password=password,
        bucket_name=bucket_name,
    ):
        return True
    return create_bucket(
        cluster_url=cluster_url,
        username=username,
        password=password,
        bucket_name=bucket_name,
        ram_quota_mb=ram_quota_mb,
        bucket_type=bucket_type,
    )