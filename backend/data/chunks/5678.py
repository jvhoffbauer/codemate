    @dataclass
    class EndpointFactory(BaseTilerFactory):
        def register_routes(self):
            """register endpoints."""

            @self.router.get("/{param2}.json")
            def route2(
                request: Request, param1: int = Path(...), param2: str = Path(...)
            ):
                """return url."""
                return {"url": self.url_for(request, "route1", param2=param2)}

            @self.router.get("/{param2}")
            def route1(param1: int = Path(...), param2: str = Path(...)):
                """return param."""
                return {"value": param2}