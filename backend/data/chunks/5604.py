    @app.get("/second")
    def _bands_expr(params=Depends(dependencies.BandsExprParams)):
        """return params."""
        return params