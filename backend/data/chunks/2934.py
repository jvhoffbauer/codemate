        @app.post("/")
        async def root(f: UploadFile = File()):
            return f  # pragma: nocover