        async def root(username: str = Form(), f: UploadFile = File()):
            return username  # pragma: nocover