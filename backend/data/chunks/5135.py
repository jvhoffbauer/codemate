def setup_index_storage(*, cluster_url, username, password):
    url = f"{cluster_url}/settings/indexes"
    auth = HTTPBasicAuth(username, password)
    r = requests.post(url, data={"storageMode": "forestdb"}, auth=auth)
    return r.status_code == 200