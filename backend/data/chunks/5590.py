    @app.get("/second")
    def _bidx_expr(params=Depends(dependencies.BidxExprParams)):
        """return params."""
        return params