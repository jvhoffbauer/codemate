def test_invalid_response_model():
    with pytest.raises(FastAPIError):
        from docs_src.response_model.tutorial003_04_py310 import app

        assert app  # pragma: no cover