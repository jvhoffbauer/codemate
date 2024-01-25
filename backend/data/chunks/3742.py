    @app.on_event("shutdown")
    def app_shutdown() -> None:
        state.app_shutdown = True