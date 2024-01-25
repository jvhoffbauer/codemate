            async def call_next():
                return await app(scope, receive, send)