def get(bucket: Bucket, *, id: str):
    doc_id = get_doc_id(id)
    return utils.get_doc(bucket=bucket, doc_id=doc_id, doc_model=ItemInDB)