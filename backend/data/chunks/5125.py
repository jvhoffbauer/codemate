def get_index(
    index_name: str,
    *,
    username: str = COUCHBASE_USER,
    password: str = COUCHBASE_PASSWORD,
    host="couchbase",
    port="8094",
):
    full_text_url = f"http://{host}:{port}"
    index_url = f"{full_text_url}/api/index/{index_name}"
    auth = HTTPBasicAuth(username, password)
    response = requests.get(index_url, auth=auth)
    if response.status_code == 400:
        content = response.json()
        error = content.get("error")
        if error == "rest_auth: preparePerms, err: index not found":
            return None
        raise ValueError(error)
    elif response.status_code == 200:
        content = response.json()
        assert (
            content.get("status") == "ok"
        ), "Expected a status OK communicating with Full Text Search"
        index_def = content.get("indexDef")
        return index_def
    raise ValueError(response.text)