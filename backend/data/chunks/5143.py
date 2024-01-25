def is_couchbase_user_created(*, cluster_url, username, password, new_user_id):
    url = f"{cluster_url}/settings/rbac/users/local/{new_user_id}"
    auth = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    return r.status_code == 200