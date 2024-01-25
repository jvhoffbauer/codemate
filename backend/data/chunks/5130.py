def get_cluster_couchbase_url(
    host="couchbase",
    port="8091",
    fetch_mutation_tokens="1",
    operation_timeout=f"{COUCHBASE_OPERATION_TIMEOUT_SECS}",
    n1ql_timeout=f"{COUCHBASE_N1QL_TIMEOUT_SECS}",
):
    # fetch_mutation_tokens becomes required to be able to do persist_to=1: https://forums.couchbase.com/t/couchbase-returns-error-on-success/14196/2
    # ref: https://docs.couchbase.com/c-sdk/2.10/client-settings.html#settings-list
    cluster_url = f"couchbase://{host}:{port}?fetch_mutation_tokens={fetch_mutation_tokens}&operation_timeout={operation_timeout}&n1ql_timeout={n1ql_timeout}"
    return cluster_url