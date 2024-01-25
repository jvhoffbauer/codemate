def upsert(bucket: Bucket, *, user_in: UserCreate, persist_to=0):
    user = upsert_in_db(bucket, user_in=user_in, persist_to=persist_to)
    user_in_sync = UserSyncIn(**user_in.dict(), name=user_in.username)
    assert insert_sync_gateway(user_in_sync)
    return user