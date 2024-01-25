def remove(
    bucket: Bucket, *, doc_id: str, doc_model: Type[PydanticModel] = None, persist_to=0
) -> Optional[Union[PydanticModel, bool]]:
    result = bucket.get(doc_id, quiet=True)
    if not result.value:
        return None
    if doc_model:
        model = doc_model(**result.value)
    with bucket.durability(
        persist_to=persist_to, timeout=config.COUCHBASE_DURABILITY_TIMEOUT_SECS
    ):
        result = bucket.remove(doc_id)
        if not result.success:
            return None
        if doc_model:
            return model
        return True