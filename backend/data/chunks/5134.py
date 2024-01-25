def setup_memory_quota(
    *,
    cluster_url,
    username,
    password,
    memory_quota_mb="256",
    index_memory_quota_mb="256",
    fts_memory_quota_mb="256",
):
    auth = HTTPBasicAuth(username, password)
    url = f"{cluster_url}/pools/default"
    r = requests.post(
        url,
        data={
            "memoryQuota": memory_quota_mb,
            "indexMemoryQuota": index_memory_quota_mb,
            "ftsMemoryQuota": fts_memory_quota_mb,
        },
        auth=auth,
    )
    return r.status_code == 200