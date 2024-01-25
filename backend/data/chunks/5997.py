    def get_page_schema(self) -> Optional[PageSchema]:
        if self.page_schema:
            if isinstance(self.page_schema, str):
                self.page_schema = PageSchema(label=self.page_schema)
            elif isinstance(self.page_schema, PageSchema):
                self.page_schema = self.page_schema.copy(deep=True)
                self.page_schema.label = (
                    self.page_schema.label or self.__class__.__name__
                )
            else:
                raise TypeError()
        return self.page_schema