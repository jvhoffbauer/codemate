def load(name: str, **json_kwargs) -> Union[str, Dict, List]:
    """Loads content from a file. If file ends with '.json', call json.load() and return a Dictionary."""
    path = DATA / name
    with open(path) as f_in:
        if path.suffix == ".json":
            return json.load(f_in, **json_kwargs)
        return f_in.read()