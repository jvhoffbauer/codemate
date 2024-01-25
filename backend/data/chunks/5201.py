def setup_routers(app: FastAPI):
    from tifa.apps import user, health, whiteboard, admin

    app.mount("/health", health.bp)
    # app.mount("/admin", admin.bp)
    app.mount("/user", user.bp)
    app.mount("/whiteboard", whiteboard.bp)
    app.mount("/metrics", make_asgi_app())