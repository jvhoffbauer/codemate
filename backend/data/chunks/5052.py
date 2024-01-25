def doc_results_to_model(
    results_from_couchbase: list, *, doc_model: Type[PydanticModel]
) -> List[PydanticModel]:
    items = []
    for doc in results_from_couchbase:
        data = doc[config.COUCHBASE_BUCKET_NAME]
        doc = doc_model(**data)
        items.append(doc)
    return items