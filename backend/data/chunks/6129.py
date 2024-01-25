    async def get_page(self, request: Request) -> Page:
        page = await super().get_page(request)
        page.body = [
            Property(
                title="SiteInfo",
                column=4,
                items=[
                    Property.Item(label="title", content=self.site.settings.site_title),
                    Property.Item(label="version", content=self.site.settings.version),
                    Property.Item(
                        label="language", content=self.site.settings.language
                    ),
                    Property.Item(label="debug", content=str(self.site.settings.debug)),
                ],
            ),
            amis.Divider(),
            Property(
                title="FastAPI-Amis-Admin",
                column=4,
                items=[
                    Property.Item(label="system", content=platform.system()),
                    Property.Item(label="python", content=platform.python_version()),
                    Property.Item(
                        label="version", content=fastapi_amis_admin.__version__
                    ),
                    Property.Item(label="license", content="Apache2.0"),
                    Property.Item(
                        label="amis-cdn", content=self.site.settings.amis_cdn
                    ),
                    Property.Item(
                        label="amis-pkg", content=self.site.settings.amis_pkg
                    ),
                    Property.Item(
                        label="amis-theme", content=self.site.settings.amis_theme
                    ),
                ],
            ),
        ]
        return page