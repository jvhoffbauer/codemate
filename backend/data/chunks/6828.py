        async def handle_exception(self, exc):
            if isinstance(exc, MyErrorToUnhandledException):
                raise MyUnhandledException("My unhandled exception")
            elif isinstance(exc, MyErrorToConvert):
                raise MyConvertedError
            else:
                raise NotImplementedError