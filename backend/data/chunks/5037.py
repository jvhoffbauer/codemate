def upsert_in_db(bucket: Bucket, *, user_in: UserCreate, persist_to=0):
    user_doc_id = get_doc_id(user_in.username)
    passwordhash = get_password_hash(user_in.password)
    user = UserInDB(**user_in.dict(), hashed_password=passwordhash)
    doc_data = jsonable_encoder(user)
    with bucket.durability(
        persist_to=persist_to, timeout=config.COUCHBASE_DURABILITY_TIMEOUT_SECS
    ):
        bucket.upsert(user_doc_id, doc_data)
    return user