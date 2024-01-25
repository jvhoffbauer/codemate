def create_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    application.add_event_handler("startup", create_redis_pool)
    application.add_event_handler("shutdown", close_redis_pool)
    return application