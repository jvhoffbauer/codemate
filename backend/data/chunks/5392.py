    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        """Handle call."""
        if scope["type"] == "http":
            request = Request(scope)

            self.logger.debug(str(request.url))

            qs = dict(request.query_params)
            if qs and self.querystrings:
                self.logger.debug(qs)

            if self.headers:
                self.logger.debug(dict(request.headers))

        await self.app(scope, receive, send)