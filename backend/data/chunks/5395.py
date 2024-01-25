        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()

            async def custom_route_handler(request: Request) -> Response:
                with rasterio.Env(**self.config):
                    response: Response = await original_route_handler(request)
                return response

            return custom_route_handler