def search(bucket: Bucket, *, query_string: str, skip=0, limit=100):
    users = utils.search_get_docs(
        bucket=bucket,
        query_string=query_string,
        index_name=full_text_index_name,
        doc_model=UserInDB,
        doc_type=USERPROFILE_DOC_TYPE,
        skip=skip,
        limit=limit,
    )
    return users