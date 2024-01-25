def is_couchbase_ready(cluster_url):
    r = requests.get(cluster_url)
    return r.status_code == 200