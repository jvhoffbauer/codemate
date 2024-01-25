def get_multi(bucket: Bucket, *, skip=0, limit=100):
    users = utils.get_docs(
        bucket=bucket,
        doc_type=USERPROFILE_DOC_TYPE,
        doc_model=UserInDB,
        skip=skip,
        limit=limit,
    )
    return users