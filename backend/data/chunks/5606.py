    @app.get("/third")
    def _bands_expr_opt(params=Depends(dependencies.BandsExprParamsOptional)):
        """return params."""
        return params