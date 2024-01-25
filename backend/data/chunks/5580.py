    @app.get("/all/{TileMatrixSetId}")
    def all(TileMatrixSetId: Literal[tuple(tms.list())] = Query(...)):
        """return tms id."""
        return TileMatrixSetId