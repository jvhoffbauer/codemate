    def get_page_schema(self) -> Optional[PageSchema]:
        if super().get_page_schema():
            assert self.src, "src is None"
            iframe = self.iframe or Iframe(src=self.src)
            if self.site.settings.site_url and iframe.src.startswith(
                self.site.settings.site_url
            ):
                self.page_schema.url = iframe.src
            else:
                self.page_schema.url = re.sub(r"^https?:", "", iframe.src)
            self.page_schema.schema_ = iframe
        return self.page_schema