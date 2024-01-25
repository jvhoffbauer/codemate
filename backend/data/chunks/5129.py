def get_cluster_http_url(host="couchbase", port="8091"):
    cluster_url = f"http://{host}:{port}"
    return cluster_url