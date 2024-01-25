    async def get_page_schema_children(self, request: Request) -> List[PageSchema]:
        page_schema_list = []
        for child in self._children:
            if not child.page_schema:
                continue
            if (isinstance(child, AdminGroup) and not isinstance(child, AdminApp)) or (
                isinstance(child, AdminApp) and child.page_schema.tabsMode is None
            ):
                sub_children = await child.get_page_schema_children(request)
                if (
                    sub_children
                ):  # If there are sub-nodes, show them even if the parent node has no permission.
                    page_schema = child.page_schema.copy(deep=True)
                    page_schema.children = sub_children
                    page_schema_list.append(page_schema)
            elif await child.has_page_permission(request, action="page"):
                page_schema_list.append(child.page_schema)
        if page_schema_list:
            page_schema_list.sort(key=lambda p: p.sort or 0, reverse=True)
        return page_schema_list