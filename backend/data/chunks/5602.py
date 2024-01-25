    @app.get("/first")
    def _bands(params=Depends(dependencies.BandsParams)):
        """return bands."""
        return params.bands