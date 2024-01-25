    async def parse_body(self, http_request) -> Any:
        try:
            req = await http_request.json()
        except ValueError:
            raise ParseError()
        return req