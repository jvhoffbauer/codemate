    @app.get("/route1")
    async def route1(value: str = Query(...)):
        """route1."""
        return {"value": value}