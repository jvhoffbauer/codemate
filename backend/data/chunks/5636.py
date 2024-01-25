    @router.get("/simple")
    def home():
        """Works and should return FALSE."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            res = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
        return {"env": res}