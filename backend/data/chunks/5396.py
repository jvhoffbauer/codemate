            async def custom_route_handler(request: Request) -> Response:
                with rasterio.Env(**self.config):
                    response: Response = await original_route_handler(request)
                return response