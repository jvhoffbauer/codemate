    @app.get("/second")
    def _assets_expr(params=Depends(dependencies.AssetsBidxExprParams)):
        """return params."""
        return params