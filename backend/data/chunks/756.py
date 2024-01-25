    async def test_view(request: Request) -> dict:
        logger.debug("Test view")
        return {"correlation_id": request.headers.get("X-Request-ID")}