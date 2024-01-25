    @sub_router.on_event("shutdown")
    def sub_router_shutdown() -> None:
        state.sub_router_shutdown = True