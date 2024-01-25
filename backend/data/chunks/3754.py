    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        state.app_startup = True
        yield
        state.app_shutdown = True