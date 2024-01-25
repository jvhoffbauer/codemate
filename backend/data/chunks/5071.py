def get_multi_by_owner(bucket: Bucket, *, owner_username: str, skip=0, limit=100):
    query_str = f"SELECT *, META().id as doc_id FROM {config.COUCHBASE_BUCKET_NAME} WHERE type = $type AND owner_username = $owner_username LIMIT $limit OFFSET $skip;"
    q = N1QLQuery(
        query_str,
        bucket=config.COUCHBASE_BUCKET_NAME,
        type=ITEM_DOC_TYPE,
        owner_username=owner_username,
        limit=limit,
        skip=skip,
    )
    q.consistency = CONSISTENCY_REQUEST
    doc_results = bucket.n1ql_query(q)
    return utils.doc_results_to_model(doc_results, doc_model=ItemInDB)