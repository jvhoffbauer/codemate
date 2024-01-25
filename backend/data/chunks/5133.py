def setup_couchbase_services(*, cluster_url, username, password):
    auth = HTTPBasicAuth(username, password)
    url = f"{cluster_url}/node/controller/setupServices"
    r = requests.post(url, data={"services": "kv,index,fts,n1ql"}, auth=auth)
    return (
        r.status_code == 200
        or "cannot change node services after cluster is provisioned" in r.text
    )