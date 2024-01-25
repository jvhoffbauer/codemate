    def amis_html(
        self,
        template_path: str = "",
        locale: str = "zh_CN",
        cdn: str = "https://unpkg.com",
        pkg: str = "amis@1.10.2",
        site_title: str = "Amis",
        site_icon: str = "",
        theme: str = "cxd",
    ):
        """Render html template"""
        template_path = template_path or self.__default_template_path__
        theme_css = (
            f'<link href="{cdn}/{pkg}/sdk/{theme}.css" rel="stylesheet"/>'
            if theme != "cxd"
            else ""
        )
        return amis_templates(template_path).safe_substitute(
            {
                "AmisSchemaJson": self.amis_json(),
                "locale": locale.replace("_", "-"),  # Fix #50
                "cdn": cdn,
                "pkg": pkg,
                "site_title": site_title,
                "site_icon": site_icon,
                "theme": theme,
                "theme_css": theme_css,
            }
        )