    @app.get("/route3")
    async def route3(response: Response):
        """route3."""
        time.sleep(1)
        response.headers["Server-Timing"] = "atime;dur=2000"
        return "I slept fine"