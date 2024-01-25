    def op(
        self, path: str, out=None, summary: str = "操作", tags: Optional[List[str]] = None
    ):
        summary = suffix_summary(path, summary)
        cls_name = "Item" + path_to_cls_name(path)
        item_schema = create_model(  # type: ignore
            cls_name,
            item=(out, ...),  # type: ignore
        )
        return self.post(path, response_model=item_schema, tags=tags, summary=summary)