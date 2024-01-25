    def get_page_schema(self) -> Optional[PageSchema]:
        if super().get_page_schema():
            assert self.link, "link is None"
            self.page_schema.link = self.page_schema.link or self.link
        return self.page_schema