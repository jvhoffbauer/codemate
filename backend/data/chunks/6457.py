    async def load(cls, name: str, **json_kwargs) -> Union[str, Dict, List]:
        """Loads content from a file. If file ends with '.json', call json.load() and return a Dictionary."""
        path = DATA / name
        async with aiofiles.open(path) as f_in:
            content = await f_in.read()
        if path.suffix == ".json":
            content = json.loads(content, **json_kwargs)
        return content