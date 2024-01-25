    @app.get("/emptytiles/{z}/{x}/{y}")
    async def emptytiles(
        z: int = Path(..., ge=0, le=30, description="Mercator tiles's zoom level"),
        x: int = Path(..., description="Mercator tiles's column"),
        y: int = Path(..., description="Mercator tiles's row"),
    ):
        """tiles."""
        return Response(status_code=404)