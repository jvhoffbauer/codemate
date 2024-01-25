def ensure_create_couchbase_user(
    *, cluster_url, username, password, new_user_id, new_user_password
):
    if is_couchbase_user_created(
        cluster_url=cluster_url,
        username=username,
        password=password,
        new_user_id=new_user_id,
    ):
        return True
    return create_couchbase_user(
        cluster_url=cluster_url,
        username=username,
        password=password,
        new_user_id=new_user_id,
        new_user_password=new_user_password,
    )