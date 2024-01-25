def get_docs_by_keys(
    bucket: Bucket, *, keys: List[str], doc_model=Type[PydanticModel]
) -> List[PydanticModel]:
    results = bucket.get_multi(keys, quiet=True)
    docs = []
    for result in results.values():
        doc = doc_model(**result.value)
        docs.append(doc)
    return docs