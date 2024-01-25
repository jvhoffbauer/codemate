def save(
    name: str,
    content: Union[str, Dict, List],
    write_mode: str = "w",
    indent: int = 2,
    **json_dumps_kwargs,
) -> pathlib.Path:
    """Save content to a file. If content is a dictionary, use json.dumps()."""
    path = DATA / name
    if isinstance(content, (dict, list)):
        content = json.dumps(content, indent=indent, **json_dumps_kwargs)
    with open(DATA / name, mode=write_mode) as f_out:
        f_out.write(content)
    return path