def test_path_param_in_prefix():
    """Test path params in prefix."""

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

    app = FastAPI()
    endpoints = EndpointFactory(reader=Reader, router_prefix="/prefixed/{param1}")
    app.include_router(endpoints.router, prefix="/prefixed/{param1}")
    client = TestClient(app)

    response = client.get("/p")
    assert response.status_code == 404

    response = client.get("/prefixed/100/value")
    assert response.json()["value"] == "value"

    response = client.get("/prefixed/100/value.json")
    assert response.json()["url"] == "http://testserver/prefixed/100/value"