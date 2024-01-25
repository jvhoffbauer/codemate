def make_app(app=None, **kwargs):
    app = app or FastAPI(**kwargs)
    app.include_router(router)
    app.include_router(prefix_router, prefix="/prefix")
    app.include_router(native_prefix_route)
    return app