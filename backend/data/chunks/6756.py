    async def parse_body(self, http_request) -> Any:
        try:
            body = await http_request.json()
        except ValueError:
            raise ParseError()

        if isinstance(body, list) and not body:
            raise InvalidRequest(
                data={
                    "errors": [
                        {
                            "loc": (),
                            "type": "value_error.empty",
                            "msg": "rpc call with an empty array",
                        }
                    ]
                }
            )

        return body