    @app.get("/", response_model=ColorMapType)
    def main(cm=Depends(dependencies.ColorMapParams)):
        """return cmap."""
        return cm