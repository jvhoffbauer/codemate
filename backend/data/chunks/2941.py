        async def root(username: str = Form(), password: str = Form()):
            return username  # pragma: nocover