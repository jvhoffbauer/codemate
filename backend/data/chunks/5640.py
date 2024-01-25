    @router.get("/future")
    def home2():
        """Doesn't work and should return the value from env."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            with futures.ThreadPoolExecutor() as executor:
                res = list(executor.map(f, range(1)))[0]
        return {"env": res}