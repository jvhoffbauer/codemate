    @classmethod
    async def save(
        cls,
        name: str,
        content: Union[str, Dict, List],
        write_mode: str = "w",
        indent: int = 2,
        **json_dumps_kwargs,
    ):
        """Save content to a file. If content is a dictionary, use json.dumps()."""
        path = DATA / name
        if isinstance(content, (dict, list)):
            content = json.dumps(content, indent=indent, **json_dumps_kwargs)
        async with aiofiles.open(DATA / name, mode=write_mode) as f_out:
            await f_out.write(content)
        return path