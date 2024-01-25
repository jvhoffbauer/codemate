def search_get_search_results(
    bucket: Bucket,
    *,
    query_string: str,
    index_name: str,
    skip: int = 0,
    limit: int = 100,
):
    if query_string:
        query = QueryStringQuery(query_string)
    else:
        query = MatchAllQuery()
    hits = bucket.search(index_name, query, fields=["*"], skip=skip, limit=limit)
    docs = []
    for hit in hits:
        docs.append(hit)
    return docs