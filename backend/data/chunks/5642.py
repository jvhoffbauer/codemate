    @router.get("/afuture")
    async def home3():
        """Works and should return FALSE."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            with futures.ThreadPoolExecutor() as executor:
                res = list(executor.map(f, range(1)))[0]
        return {"env": res}