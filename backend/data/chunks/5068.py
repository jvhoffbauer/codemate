def update(
    bucket: Bucket,
    *,
    id: str,
    doc_in: ItemUpdate,
    owner_username=None,
    persist_to=0,
    ttl=0,
):
    doc_id = get_doc_id(id=id)
    doc = get(bucket, id=id)
    doc = doc.copy(update=doc_in.dict(skip_defaults=True))
    if owner_username is not None:
        doc.owner_username = owner_username
    return utils.upsert(
        bucket=bucket, doc_id=doc_id, doc_in=doc, persist_to=persist_to, ttl=ttl
    )