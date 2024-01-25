def setup_couchbase_username_password(*, cluster_url, username, password):
    url = f"{cluster_url}/settings/web"
    auth = HTTPBasicAuth(COUCHBASE_DEFAULT_USER, COUCHBASE_DEFAULT_PASSWORD)
    r = requests.post(
        url,
        data={"username": username, "password": password, "port": "SAME"},
        auth=auth,
    )
    return r.status_code == 200