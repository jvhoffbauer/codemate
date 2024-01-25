    def as_page_body(
        self, group_extra: Dict[str, Any] = None, item_extra: Dict[str, Any] = None
    ):
        if self.children:
            exclude = {
                "type",
                "url",
                "schema_",
                "schemaApi",
                "link",
                "redirect",
                "rewrite",
                "isDefaultPage",
                "children",
            }
            if self.tabsMode is None:
                body = App(pages=[PageSchema(children=self.children)])
            elif self.tabsMode == TabsModeEnum.collapse:
                body = (
                    CollapseGroup.parse_obj(
                        self.dict(exclude=exclude, exclude_defaults=True)
                    )
                    .update_from_kwargs(
                        body=[
                            CollapseGroup.CollapseItem.parse_obj(
                                item.dict(exclude=exclude, exclude_defaults=True)
                            )
                            .update_from_kwargs(
                                header=item.label,
                                body=item.as_page_body(group_extra, item_extra),
                            )
                            .update_from_dict(item_extra or {})
                            for item in self.children
                        ],
                    )
                    .update_from_dict(group_extra or {})
                )
            else:
                body = (
                    Tabs.parse_obj(self.dict(exclude=exclude, exclude_defaults=True))
                    .update_from_kwargs(
                        mountOnEnter=True,
                        tabs=[
                            Tabs.Item.parse_obj(
                                item.dict(exclude=exclude, exclude_defaults=True)
                            )
                            .update_from_kwargs(
                                title=item.label,
                                tab=item.as_page_body(group_extra, item_extra),
                            )
                            .update_from_dict(item_extra or {})
                            for item in self.children
                        ],
                    )
                    .update_from_dict(group_extra or {})
                )
        elif self.schema_:
            body = self.schema_
            if isinstance(body, Iframe):
                body.height = body.height or 1080
        elif self.schemaApi:
            body = Service(schemaApi=self.schemaApi)
        elif self.link:
            body = Page(body=Link(href=self.link, body=self.label, blank=True))
        else:
            body = None
        return body