def create_bucket(
    *,
    cluster_url,
    username,
    password,
    bucket_name,
    ram_quota_mb=100,
    bucket_type="couchbase",
):
    url = f"{cluster_url}/pools/default/buckets"
    auth = HTTPBasicAuth(username, password)
    data = {"name": bucket_name, "ramQuotaMB": ram_quota_mb, "bucketType": bucket_type}
    r = requests.post(url, data=data, auth=auth)
    return r.status_code == 202