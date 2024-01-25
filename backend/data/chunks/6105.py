    async def _get_page_as_app(self, request: Request) -> App:
        app = App()
        app.brandName = self.site.settings.site_title
        app.logo = self.site.settings.site_icon
        app.header = Tpl(
            className="w-full",
            tpl='<div class="flex justify-between"><div></div>'
            f'<div><a href="{fastapi_amis_admin.__url__}" target="_blank" '
            'title="Copyright"><i class="fa fa-github fa-2x"></i></a></div></div>',
        )
        app.footer = (
            '<div class="p-2 text-center bg-light">Copyright © 2021 - 2022  '
            f'<a href="{fastapi_amis_admin.__url__}" target="_blank" '
            'class="link-secondary">fastapi-amis-admin</a>. All rights reserved. '
            f'<a target="_blank" href="{fastapi_amis_admin.__url__}" '
            f'class="link-secondary" rel="noopener">v{fastapi_amis_admin.__version__}</a></div> '
        )
        # app.asideBefore = '<div class="p-2 text-center">菜单前面区域</div>'
        # app.asideAfter = f'<div class="p-2 text-center">' \
        #                  f'<a href="{fastapi_amis_admin.__url__}"  target="_blank">fastapi-amis-admin</a></div>'
        children = await self.get_page_schema_children(request)
        app.pages = [{"children": children}] if children else []
        return app