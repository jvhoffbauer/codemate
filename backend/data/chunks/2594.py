def test_invalid_response_model_raises():
    with pytest.raises(FastAPIError):
        app = FastAPI()

        @app.get("/", response_model=NonPydanticModel)
        def read_root():
            pass  # pragma: nocover