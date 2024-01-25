    def setup(self) -> None:
        super().setup()

        if self.openrpc_url:
            assert self.title, "A title must be provided for OpenRPC, e.g.: 'My API'"
            assert self.version, "A version must be provided for OpenRPC, e.g.: '2.1.0'"

            async def openrpc(_: Request) -> JSONResponse:
                return JSONResponse(self.openrpc())

            self.add_route(self.openrpc_url, openrpc, include_in_schema=False)