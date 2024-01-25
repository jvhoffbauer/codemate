    def get_page_schema(self) -> Optional[PageSchema]:
        if super().get_page_schema():
            if self.page_schema.tabsMode is None:
                self.page_schema.schemaApi = None
        return self.page_schema