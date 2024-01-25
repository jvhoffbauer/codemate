    @app.get("/route2")
    async def route2():
        """route2."""
        time.sleep(1)
        return "I slept fine"