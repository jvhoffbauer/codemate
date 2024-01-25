        @app.get("/", response_model=NonPydanticModel)
        def read_root():
            pass  # pragma: nocover