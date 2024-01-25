    def mount_app(
        self,
        fastapi: FastAPI,
        *,
        name: str = "admin",
        enable_exception_handlers: bool = True,
        enable_db_middleware: bool = True,
    ) -> None:
        """
        Mount app to fastapi, the path is: site.settings.site_path.
        Once mount, the site will create all registered admin instance and register router.
        If the middleware is not enabled, please register the site.db database middleware in the appropriate location outside.
        Args:
            fastapi (FastAPI): The FastAPI instance to mount the admin app on.
            name (str, optional): The name of the app. Defaults to "admin".
            enable_exception_handlers (bool, optional): Whether to enable exception handlers. Defaults to True.
            enable_db_middleware (bool, optional): Whether to enable database middleware. Defaults to True.
        """
        self.application = fastapi
        self.register_router()
        fastapi.mount(self.settings.site_path, self.fastapi, name=name)
        if enable_exception_handlers:
            register_exception_handlers(self.fastapi)
        if enable_db_middleware:
            self.db.attach_middleware(fastapi)
        """Add SQLAlchemy Session middleware to the main application, and the session object will be bound to each request.
        Note:
        1. The session will be automatically closed when the request ends, so you don't need to close it manually.
        2. In the sub-application, you can also use this middleware, but you need to pay attention that the session object
        in the sub-application will be closed in the main application.
        3. If the sub-application needs to use its own session object, you need to add this middleware to the sub-application.
        4. Middleware or routes after this middleware can get the session object through `db.session`.
        """