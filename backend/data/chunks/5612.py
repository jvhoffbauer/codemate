    @app.get("/", response_class=JSONResponse)
    def _endpoint(params=Depends(dependencies.DatasetParams)):
        """return params."""
        return params