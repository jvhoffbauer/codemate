def ensure_create_full_text_indexes(
    index_dir=COUCHBASE_FULL_TEXT_INDEX_DEFINITIONS_DIR,
    username: str = COUCHBASE_USER,
    password: str = COUCHBASE_PASSWORD,
    host="couchbase",
    port="8094",
):
    file_path: PurePath
    for file_path in Path(index_dir).iterdir():
        if file_path.name.endswith(".json"):
            with open(file_path) as f:
                index_definition = json.load(f)
            name = index_definition.get("name")
            assert name, "A full text search index definition must have a name field"
            current_index = get_index(
                index_name=name,
                username=username,
                password=password,
                host=host,
                port=port,
            )
            if not current_index:
                assert create_index(
                    index_definition=index_definition,
                    username=username,
                    password=password,
                    host=host,
                    port=port,
                ), "Full Text Search index could not be created"