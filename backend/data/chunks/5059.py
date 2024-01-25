def search_get_doc_ids(
    bucket: Bucket,
    *,
    query_string: str,
    index_name: str,
    skip: int = 0,
    limit: int = 100,
) -> List[str]:
    query = QueryStringQuery(query_string)
    hits = bucket.search(index_name, query, skip=skip, limit=limit)
    doc_ids = []
    for hit in hits:
        doc_ids.append(hit["id"])
    return doc_ids