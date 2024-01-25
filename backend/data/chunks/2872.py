        @app.get("/")
        def read_root() -> Union[Response, None]:
            return Response(content="Foo")  # pragma: no cover