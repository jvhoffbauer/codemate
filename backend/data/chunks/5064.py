def search_by_type_get_results_to_docs(
    bucket: Bucket,
    *,
    query_string: str,
    index_name: str,
    doc_type: str,
    doc_model: Type[PydanticModel],
    skip=0,
    limit=100,
) -> List[PydanticModel]:
    doc_results = search_by_type_get_search_results(
        bucket=bucket,
        query_string=query_string,
        index_name=index_name,
        doc_type=doc_type,
        skip=skip,
        limit=limit,
    )
    return search_results_to_model(doc_results, doc_model=doc_model)