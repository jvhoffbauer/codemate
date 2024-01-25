    def _endpoint(algorithm=Depends(PostProcessParams)):
        """return params."""
        if algorithm:
            return algorithm.dict()
        return {}