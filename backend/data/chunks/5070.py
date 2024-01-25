def get_multi(bucket: Bucket, *, skip=0, limit=100):
    return utils.get_docs(
        bucket=bucket,
        doc_type=ITEM_DOC_TYPE,
        doc_model=ItemInDB,
        skip=skip,
        limit=limit,
    )