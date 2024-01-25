def get_doc_results_by_type(bucket: Bucket, *, doc_type: str, skip=0, limit=100):
    query_str = f"SELECT *, META().id as doc_id FROM {config.COUCHBASE_BUCKET_NAME} WHERE type = $type LIMIT $limit OFFSET $skip;"
    q = N1QLQuery(
        query_str,
        bucket=config.COUCHBASE_BUCKET_NAME,
        type=doc_type,
        limit=limit,
        skip=skip,
    )
    q.consistency = CONSISTENCY_REQUEST
    result = bucket.n1ql_query(q)
    return result