    def get_page_schema(self) -> Optional[PageSchema]:
        if super().get_page_schema():
            self.page_schema.url = f"{self.router_path}{self.page_path}"
            self.page_schema.schemaApi = AmisAPI(
                method="post",
                url=f"{self.router_path}{self.page_path}",
                data={},
                cache=300000,
            )
            if self.page_parser_mode == "html":
                self.page_schema.schema_ = Iframe(src=self.page_schema.url)
        return self.page_schema