def get_by_email(bucket: Bucket, *, email: str):
    query_str = f"SELECT *, META().id as doc_id FROM {config.COUCHBASE_BUCKET_NAME} WHERE type = $type AND email = $email;"
    q = N1QLQuery(
        query_str,
        bucket=config.COUCHBASE_BUCKET_NAME,
        type=USERPROFILE_DOC_TYPE,
        email=email,
    )
    q.consistency = CONSISTENCY_REQUEST
    doc_results = bucket.n1ql_query(q)
    users = utils.doc_results_to_model(doc_results, doc_model=UserInDB)
    if not users:
        return None
    return users[0]