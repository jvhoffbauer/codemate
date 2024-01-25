def update(bucket: Bucket, *, username: str, user_in: UserUpdate, persist_to=0):
    user = update_in_db(
        bucket, username=username, user_in=user_in, persist_to=persist_to
    )
    user_in_sync_data = user.dict()
    user_in_sync_data.update({"name": user.username})
    if user_in.password:
        user_in_sync_data.update({"password": user_in.password})
    user_in_sync = UserSyncIn(**user_in_sync_data)
    assert update_sync_gateway(user_in_sync)
    return user