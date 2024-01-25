        @app.get("/", response_model=List[NonPydanticModel])
        def read_root():
            pass  # pragma: nocover