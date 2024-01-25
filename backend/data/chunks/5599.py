    @app.get("/third")
    def _assets_bidx(params=Depends(dependencies.AssetsBidxParams)):
        """return params."""
        return params