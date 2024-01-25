    @ep.method()
    def probe() -> str:
        raise HTTPException(401)