def search_get_docs(
    bucket: Bucket,
    *,
    query_string: str,
    index_name: str,
    doc_model: Type[PydanticModel],
    doc_type: str = None,
    skip=0,
    limit=100,
) -> List[PydanticModel]:
    if doc_type is not None:
        type_filter = f"type:{doc_type}"
        if not query_string:
            query_string = type_filter
        if query_string and type_filter not in query_string:
            query_string += f" {type_filter}"
    keys = search_get_doc_ids(
        bucket=bucket,
        query_string=query_string,
        index_name=index_name,
        skip=skip,
        limit=limit,
    )
    if not keys:
        return []
    return get_docs_by_keys(bucket=bucket, keys=keys, doc_model=doc_model)