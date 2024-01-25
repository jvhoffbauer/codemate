def ensure_couchbase_username_password(*, cluster_url, username, password):
    if setup_couchbase_username_password(
        cluster_url=cluster_url, username=username, password=password
    ):
        return True
    return check_couchbase_username_password(
        cluster_url=cluster_url, username=username, password=password
    )