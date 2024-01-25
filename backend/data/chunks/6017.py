    async def page_parser(self, request: Request, page: Dict[str, Any]) -> Response:
        page["request"] = request
        return self.templates.TemplateResponse(self.template_name, page)