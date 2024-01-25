def update_sync_gateway(user: UserSyncIn):
    name = user.name
    url = f"http://{config.COUCHBASE_SYNC_GATEWAY_HOST}:{config.COUCHBASE_SYNC_GATEWAY_PORT}/{config.COUCHBASE_SYNC_GATEWAY_DATABASE}/_user/{name}"
    if user.password:
        data = jsonable_encoder(user)
    else:
        data = jsonable_encoder(user, exclude={"password"})
    response = requests.put(url, json=data)
    return response.status_code == 200 or response.status_code == 201