    @app.get("/tiles/{z}/{x}/{y}")
    async def tiles(
        z: int = Path(..., ge=0, le=30, description="Mercator tiles's zoom level"),
        x: int = Path(..., description="Mercator tiles's column"),
        y: int = Path(..., description="Mercator tiles's row"),
    ):
        """tiles."""
        return "yeah"