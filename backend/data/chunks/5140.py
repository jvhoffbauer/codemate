def is_bucket_created(*, cluster_url, username, password, bucket_name):
    url = f"{cluster_url}/pools/default/buckets/{bucket_name}"
    auth = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    return r.status_code == 200