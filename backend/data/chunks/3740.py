    @app.on_event("startup")
    def app_startup() -> None:
        state.app_startup = True