    def _endpoint(params=Depends(dependencies.ImageParams)):
        """return params."""
        return params