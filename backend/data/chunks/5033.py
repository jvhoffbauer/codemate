def get(bucket: Bucket, *, username: str):
    doc_id = get_doc_id(username)
    return utils.get_doc(bucket=bucket, doc_id=doc_id, doc_model=UserInDB)