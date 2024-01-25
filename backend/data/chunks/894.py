    def build_middleware_stack(self) -> ASGIApp:
        # Duplicate/override from Starlette to add AsyncExitStackMiddleware
        # inside of ExceptionMiddleware, inside of custom user middlewares
        debug = self.debug
        error_handler = None
        exception_handlers = {}

        for key, value in self.exception_handlers.items():
            if key in (500, Exception):
                error_handler = value
            else:
                exception_handlers[key] = value

        middleware = (
            [Middleware(ServerErrorMiddleware, handler=error_handler, debug=debug)]
            + self.user_middleware
            + [
                Middleware(
                    ExceptionMiddleware, handlers=exception_handlers, debug=debug
                ),
                # Add FastAPI-specific AsyncExitStackMiddleware for dependencies with
                # contextvars.
                # This needs to happen after user middlewares because those create a
                # new contextvars context copy by using a new AnyIO task group.
                # The initial part of dependencies with 'yield' is executed in the
                # FastAPI code, inside all the middlewares. However, the teardown part
                # (after 'yield') is executed in the AsyncExitStack in this middleware.
                # If the AsyncExitStack lived outside of the custom middlewares and
                # contextvars were set in a dependency with 'yield' in that internal
                # contextvars context, the values would not be available in the
                # outer context of the AsyncExitStack.
                # By placing the middleware and the AsyncExitStack here, inside all
                # user middlewares, the code before and after 'yield' in dependencies
                # with 'yield' is executed in the same contextvars context. Thus, all values
                # set in contextvars before 'yield' are still available after 'yield,' as
                # expected.
                # Additionally, by having this AsyncExitStack here, after the
                # ExceptionMiddleware, dependencies can now catch handled exceptions,
                # e.g. HTTPException, to customize the teardown code (e.g. DB session
                # rollback).
                Middleware(AsyncExitStackMiddleware),
            ]
        )

        app = self.router
        for cls, options in reversed(middleware):
            app = cls(app=app, **options)
        return app