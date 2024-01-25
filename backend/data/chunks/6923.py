    @ep.method()
    def probe() -> str:
        return credentials_var.get().username