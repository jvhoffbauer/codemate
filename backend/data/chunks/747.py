    async def test_view():
        logger.debug("Test view")
        task1.delay().get(timeout=10)