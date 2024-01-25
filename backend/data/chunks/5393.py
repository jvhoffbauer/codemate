    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        """Handle call."""
        if scope["type"] == "http":
            request = Request(scope)

            DECODE_FORMAT = "latin-1"

            query_string = ""
            for k, v in request.query_params.multi_items():
                query_string += k.lower() + "=" + v + "&"

            query_string = query_string[:-1]
            request.scope["query_string"] = query_string.encode(DECODE_FORMAT)

        await self.app(scope, receive, send)