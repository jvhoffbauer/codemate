def search_with_owner(
    bucket: Bucket, *query_string: str, username: str, skip=0, limit=100
):
    username_filter = f"owner_username:{username}"
    if username_filter not in query_string:
        query_string = f"{query_string} {username_filter}"
    docs = utils.search_get_docs(
        bucket=bucket,
        query_string=query_string,
        index_name=full_text_index_name,
        doc_model=ItemInDB,
        skip=skip,
        limit=limit,
    )
    return docs