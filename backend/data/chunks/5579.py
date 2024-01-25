    def web(TileMatrixSetId: Literal["WebMercatorQuad"] = Query(...)):
        """return tms id."""
        return TileMatrixSetId