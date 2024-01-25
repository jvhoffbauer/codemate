    def page(self, path, out, summary: str = "Page", tags: Optional[List[str]] = None):
        if "-Page" not in summary:
            summary = summary + "-Page"
        cls_name = "Page" + path_to_cls_name(path)
        page_schema = create_model(  # type: ignore
            cls_name,
            items=(list[out], ...),  # type: ignore
            page=(Optional[int], ...),
            per_page=(Optional[int], ...),
            total=(Optional[int], ...),
            __base__=APIModel,
        )
        return self.get(path, response_model=page_schema, tags=tags, summary=summary)