def check_couchbase_username_password(*, cluster_url, username, password):
    url = f"{cluster_url}/settings/web"
    auth = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    return r.status_code == 200