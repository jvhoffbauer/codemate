def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
    )
    # thread local just flask like g
    app.add_middleware(GlobalsMiddleware)
    # 注册 db models
    setup_db_models(app)
    # 初始化路由
    setup_routers(app)
    # 初始化静态资源路径
    setup_static_files(app)
    # 初始化全局 middleware
    setup_middleware(app)
    # 初始化全局 middleware
    setup_logging(app)
    # 初始化 sentry
    if settings.SENTRY_DSN:
        setup_sentry(app)

    return app