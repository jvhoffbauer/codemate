    @app.get("/test", status_code=200)
    async def test_view() -> dict:
        logger.debug("Test view")
        return {"test": "test"}