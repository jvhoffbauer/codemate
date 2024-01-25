    @sub_router.on_event("startup")
    def sub_router_startup() -> None:
        state.sub_router_startup = True