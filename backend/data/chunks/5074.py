def search_get_search_results_to_docs(
    bucket: Bucket, *, query_string: str, skip=0, limit=100
):
    docs = utils.search_by_type_get_results_to_docs(
        bucket=bucket,
        query_string=query_string,
        index_name=full_text_index_name,
        doc_type=ITEM_DOC_TYPE,
        doc_model=ItemInDB,
        skip=skip,
        limit=limit,
    )
    return docs