def update_in_db(bucket: Bucket, *, username: str, user_in: UserUpdate, persist_to=0):
    user_doc_id = get_doc_id(username)
    stored_user = get(bucket, username=username)
    stored_user = stored_user.copy(update=user_in.dict(skip_defaults=True))
    if user_in.password:
        passwordhash = get_password_hash(user_in.password)
        stored_user.hashed_password = passwordhash
    data = jsonable_encoder(stored_user)
    with bucket.durability(
        persist_to=persist_to, timeout=config.COUCHBASE_DURABILITY_TIMEOUT_SECS
    ):
        bucket.upsert(user_doc_id, data)
    return stored_user