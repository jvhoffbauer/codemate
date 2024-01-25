def search_results_to_model(
    results_from_couchbase: list, *, doc_model: Type[PydanticModel]
) -> List[PydanticModel]:
    items = []
    for doc in results_from_couchbase:
        data = doc.get("fields")
        if not data:
            continue
        data_nones = {}
        for key, value in data.items():
            field: Field = doc_model.__fields__[key]
            if not value:
                value = None
            elif field.shape in {SHAPE_LIST, SHAPE_SET, SHAPE_TUPLE} and not isinstance(
                value, list
            ):
                value = [value]
            data_nones[key] = value
        doc = doc_model(**data_nones)
        items.append(doc)
    return items