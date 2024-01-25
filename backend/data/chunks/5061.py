def search_by_type_get_search_results(
    bucket: Bucket,
    *,
    query_string: str,
    index_name: str,
    doc_type: str,
    skip: int = 0,
    limit: int = 100,
):
    type_filter = f"type:{doc_type}"
    if not query_string:
        query_string = type_filter
    if query_string and type_filter not in query_string:
        query_string += f" {type_filter}"
    query = QueryStringQuery(query_string)
    hits = bucket.search(index_name, query, fields=["*"], skip=skip, limit=limit)
    docs = []
    for hit in hits:
        docs.append(hit)
    return docs