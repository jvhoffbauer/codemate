def import_couchbase_default_data(*, cluster_url, username, password):
    url = f"{cluster_url}/sampleBuckets/install"
    auth = HTTPBasicAuth(username, password)
    r = requests.post(url, json=["travel-sample"], auth=auth)
    return (
        r.status_code == 202
        or f"Sample bucket {COUCHBASE_DEFAULT_DATASET} is already loaded." in r.text
    )