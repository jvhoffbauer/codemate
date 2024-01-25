def doc_result_to_model(
    couchbase_result, *, doc_model: Type[PydanticModel]
) -> PydanticModel:
    data = couchbase_result[config.COUCHBASE_BUCKET_NAME]
    doc = doc_model(**data)
    return doc