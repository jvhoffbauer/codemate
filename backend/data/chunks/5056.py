def upsert(
    bucket: Bucket, *, doc_id: str, doc_in: PydanticModel, persist_to=0, ttl=0
) -> Optional[PydanticModel]:
    doc_data = jsonable_encoder(doc_in)
    with bucket.durability(
        persist_to=persist_to, timeout=config.COUCHBASE_DURABILITY_TIMEOUT_SECS
    ):
        result = bucket.upsert(doc_id, doc_data, ttl=ttl)
        if result.success:
            return doc_in
    return None