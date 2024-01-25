    async def page_parser(self, request: Request, page: Page) -> Response:
        if request.method == "GET":
            result = page.amis_html(
                template_path=self.template_name,
                locale=_.get_language(),
                cdn=self.site.settings.amis_cdn,
                pkg=self.site.settings.amis_pkg,
                theme=self.site.settings.amis_theme,
                site_title=self.site.settings.site_title,
                site_icon=self.site.settings.site_icon,
            )
            result = HTMLResponse(result)
        else:
            data = page.amis_dict()
            if await request.body():
                data = deep_update(data, (await request.json()).get("_update", {}))
            result = BaseAmisApiOut(data=data)
            result = JSONResponse(result.dict())
        return result