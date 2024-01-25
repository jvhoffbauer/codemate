    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)