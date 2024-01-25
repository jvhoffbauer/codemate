        async def root(username: str = Form()):
            return username  # pragma: nocover