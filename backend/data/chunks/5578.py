    @app.get("/web/{TileMatrixSetId}")
    def web(TileMatrixSetId: Literal["WebMercatorQuad"] = Query(...)):
        """return tms id."""
        return TileMatrixSetId