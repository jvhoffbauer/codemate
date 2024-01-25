def remove(bucket: Bucket, *, id: str, persist_to=0):
    doc_id = get_doc_id(id)
    return utils.remove(
        bucket=bucket, doc_id=doc_id, doc_model=ItemInDB, persist_to=persist_to
    )