def test_invalid_response_model_in_responses_raises():
    with pytest.raises(FastAPIError):
        app = FastAPI()

        @app.get("/", responses={"500": {"model": NonPydanticModel}})
        def read_root():
            pass  # pragma: nocover