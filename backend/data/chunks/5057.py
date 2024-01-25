def update(
    bucket: Bucket,
    *,
    doc_id: str,
    doc: PydanticModel,
    doc_updated: PydanticModel,
    persist_to=0,
    ttl=0,
):
    doc_updated = doc.copy(update=doc_updated.dict(skip_defaults=True))
    data = jsonable_encoder(doc_updated)
    with bucket.durability(
        persist_to=persist_to, timeout=config.COUCHBASE_DURABILITY_TIMEOUT_SECS
    ):
        result = bucket.upsert(doc_id, data, ttl=ttl)
        if result.success:
            return doc_updated