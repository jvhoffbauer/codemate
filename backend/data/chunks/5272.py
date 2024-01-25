    def list(self, path, out, summary: str = "List", tags: Optional[list[str]] = None):
        if "-List" not in summary:
            summary = summary + "-List"
        cls_name = "List" + path_to_cls_name(path)
        list_schema = create_model(  # type: ignore
            cls_name,
            items=(list[out], ...),  # type: ignore
        )
        return self.get(path, response_model=list_schema, tags=tags, summary=summary)