    def middleware_constructor(app):
        @functools.wraps(app)
        async def wrapped_app(scope, receive, send):
            if scope["type"] != "websocket":
                return await app(scope, receive, send)  # pragma: no cover

            async def call_next():
                return await app(scope, receive, send)

            websocket = WebSocket(scope, receive=receive, send=send)
            return await middleware_func(websocket, call_next)

        return wrapped_app