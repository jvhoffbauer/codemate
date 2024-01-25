    @app.get("/first")
    def _bidx(params=Depends(dependencies.BidxParams)):
        """return indexes."""
        return params.indexes