    @default_app.get("/celery-test", status_code=200)
    async def test_view():
        logger.debug("Test view")
        task1.delay().get(timeout=10)