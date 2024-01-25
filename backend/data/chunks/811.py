async def extract_entities_by_type(
    body: RecordsRequest = Body(..., example=example_request)
):
    """Extract Named Entities from a batch of Records separated by entity label.
    This route can be used directly as a Cognitive Skill in Azure Search
    For Documentation on integration with Azure Search, see here:
    https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface
    """

    res = []
    documents = []

    for val in body.values:
        documents.append({"id": val.recordId, "text": val.data.text})

    entities_res = extractor.extract_entities(documents)
    res = []

    for er in entities_res:
        groupby = defaultdict(list)
        for ent in er["entities"]:
            ent_prop = ENT_PROP_MAP[ent["label"]]
            groupby[ent_prop].append(ent["name"])
        record = {"recordId": er["id"], "data": groupby}
        res.append(record)

    return {"values": res}