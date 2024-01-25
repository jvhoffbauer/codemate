    @router.get("/afuture")
    async def home3():
        """Works and should return FALSE."""
        with futures.ThreadPoolExecutor() as executor:
            res = list(executor.map(f, range(1)))[0]
        return {"env": res}