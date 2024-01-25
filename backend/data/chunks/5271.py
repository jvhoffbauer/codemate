    def item(self, path, out, summary: str = "Item", tags: Optional[list[str]] = None):
        if "-Item" not in summary:
            summary = summary + "-Item"
        cls_name = "Item" + path_to_cls_name(path)
        item_schema = create_model(  # type: ignore
            cls_name,
            item=(out, ...),
        )
        return self.get(path, response_model=item_schema, tags=tags, summary=summary)