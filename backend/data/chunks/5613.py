    def _endpoint(params=Depends(dependencies.DatasetParams)):
        """return params."""
        return params