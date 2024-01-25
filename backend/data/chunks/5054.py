def get_docs(
    bucket: Bucket, *, doc_type: str, doc_model=Type[PydanticModel], skip=0, limit=100
) -> List[PydanticModel]:
    doc_results = get_doc_results_by_type(
        bucket, doc_type=doc_type, skip=skip, limit=limit
    )
    return doc_results_to_model(doc_results, doc_model=doc_model)