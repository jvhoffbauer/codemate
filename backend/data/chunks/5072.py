def search(bucket: Bucket, *, query_string: str, skip=0, limit=100):
    docs = utils.search_get_docs(
        bucket=bucket,
        query_string=query_string,
        index_name=full_text_index_name,
        doc_model=ItemInDB,
        skip=skip,
        limit=limit,
    )
    return docs