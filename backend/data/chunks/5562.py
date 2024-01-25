    async def route1(value: List[str] = Query(...)):
        """route1."""
        return {"value": value}