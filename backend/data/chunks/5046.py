def search_get_search_results_to_docs(
    bucket: Bucket, *, query_string: str, skip=0, limit=100
):
    users = utils.search_by_type_get_results_to_docs(
        bucket=bucket,
        query_string=query_string,
        index_name=full_text_index_name,
        doc_type=USERPROFILE_DOC_TYPE,
        doc_model=UserInDB,
        skip=skip,
        limit=limit,
    )
    return users