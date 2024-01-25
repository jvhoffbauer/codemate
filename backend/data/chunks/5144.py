def create_couchbase_user(
    *, cluster_url, username, password, new_user_id, new_user_password
):
    url = f"{cluster_url}/settings/rbac/users/local/{new_user_id}"
    auth = HTTPBasicAuth(username, password)
    data = {
        "name": "",
        "roles": "ro_admin,bucket_full_access[*]",
        "password": new_user_password,
    }
    r = requests.put(url, data=data, auth=auth)
    return r.status_code == 200