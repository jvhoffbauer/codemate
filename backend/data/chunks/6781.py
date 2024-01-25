            async def openrpc(_: Request) -> JSONResponse:
                return JSONResponse(self.openrpc())