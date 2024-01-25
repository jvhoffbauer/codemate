    @app.get("/nan", response_class=JSONResponse)
    def is_nan(params=Depends(dependencies.DatasetParams)):
        """return params."""
        return str(params.nodata)