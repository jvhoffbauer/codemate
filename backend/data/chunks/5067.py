def upsert(
    bucket: Bucket,
    *,
    id: str,
    doc_in: ItemCreate,
    owner_username: str,
    persist_to=0,
    ttl=0,
):
    doc_id = get_doc_id(id)
    doc = ItemInDB(**doc_in.dict(), id=id, owner_username=owner_username)
    return utils.upsert(
        bucket=bucket, doc_id=doc_id, doc_in=doc, persist_to=persist_to, ttl=ttl
    )