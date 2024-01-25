    @router.on_event("shutdown")
    def router_shutdown() -> None:
        state.router_shutdown = True