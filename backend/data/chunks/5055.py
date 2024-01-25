def get_doc(
    bucket: Bucket, *, doc_id: str, doc_model: Type[PydanticModel]
) -> Optional[PydanticModel]:
    result = bucket.get(doc_id, quiet=True)
    if not result.value:
        return None
    model = doc_model(**result.value)
    return model