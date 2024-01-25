        async def route(
            request: Request,
            page: self.AnnotatedPage,  # type:ignore
        ):
            return await self.page_parser(request, page)