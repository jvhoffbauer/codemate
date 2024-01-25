    def main(cm=Depends(dependencies.ColorMapParams)):
        """return cmap."""
        return cm