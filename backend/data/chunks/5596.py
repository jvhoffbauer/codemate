    def _assets(params=Depends(dependencies.AssetsParams)):
        """return assets."""
        return params.assets