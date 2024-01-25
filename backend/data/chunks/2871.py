def test_invalid_response_model_field():
    app = FastAPI()
    with pytest.raises(FastAPIError) as e:

        @app.get("/")
        def read_root() -> Union[Response, None]:
            return Response(content="Foo")  # pragma: no cover

    assert "valid Pydantic field type" in e.value.args[0]
    assert "parameter response_model=None" in e.value.args[0]