    @router.on_event("startup")
    def router_startup() -> None:
        state.router_startup = True