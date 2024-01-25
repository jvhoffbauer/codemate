def create_index(
    index_definition: Dict[str, Any],
    *,
    reset_uuids=True,
    username: str = COUCHBASE_USER,
    password: str = COUCHBASE_PASSWORD,
    host="couchbase",
    port="8094",
):
    index_name = index_definition.get("name")
    assert index_name, "An index name is required as key in an index definition"
    if reset_uuids:
        index_definition.update({"uuid": "", "sourceUUID": ""})
    full_text_url = f"http://{host}:{port}"
    index_url = f"{full_text_url}/api/index/{index_name}"
    auth = HTTPBasicAuth(username, password)
    response = requests.put(index_url, auth=auth, json=index_definition)
    content = response.json()
    if response.status_code == 400:
        error = content.get("error")
        if (
            "cannot create index because an index with the same name already exists:"
            in error
        ):
            raise ValueError(error)
        else:
            raise ValueError(error)
    elif response.status_code == 200:
        assert (
            content.get("status") == "ok"
        ), "Expected a status OK communicating with Full Text Search"
        return True
    raise ValueError(response.text)