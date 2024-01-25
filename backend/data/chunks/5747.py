def read_json_fixture(fname: str) -> Dict[Any, Any]:
    """Read json from test directory."""
    with open(os.path.join(DATA_DIR, fname)) as f:
        return json.load(f)